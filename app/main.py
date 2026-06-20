from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tarefas = []
proximo_id = 1


class TarefaCreate(BaseModel):
    titulo: str


class TarefaUpdate(BaseModel):
    titulo: str
    concluida: bool


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tarefas", status_code=201)
def criar_tarefa(tarefa: TarefaCreate):
    global proximo_id

    nova_tarefa = {
        "id": proximo_id,
        "titulo": tarefa.titulo,
        "concluida": False
    }

    tarefas.append(nova_tarefa)
    proximo_id += 1

    return nova_tarefa


@app.get("/tarefas/{id}")
def buscar_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            return tarefa

    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@app.get("/tarefas")
def listar_tarefas():
    return tarefas


@app.put("/tarefas/{id}")
def atualizar_tarefa(id: int, dados: TarefaUpdate):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["titulo"] = dados.titulo
            tarefa["concluida"] = dados.concluida
            return tarefa

    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
