from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Store em memória. Zera quando o processo reinicia.
_tarefas: dict[int, dict] = {}
_proximo_id = 1


class TarefaIn(BaseModel):
    titulo: str


class TarefaUpdate(BaseModel):
    titulo: str
    concluida: bool


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tarefas", status_code=201)
def criar(tarefa: TarefaIn):
    global _proximo_id
    nova = {"id": _proximo_id, "titulo": tarefa.titulo, "concluida": False}
    _tarefas[_proximo_id] = nova
    _proximo_id += 1
    return nova


# --- Implementações do Exercício ---


@app.get("/tarefas")
def listar_todas():
    # Retorna uma lista com todas as tarefas armazenadas no dicionário
    return list(_tarefas.values())


@app.get("/tarefas/{tarefa_id}")
def obter_por_id(tarefa_id: int):
    # Verifica se a tarefa existe no dicionário
    if tarefa_id not in _tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return _tarefas[tarefa_id]


@app.put("/tarefas/{tarefa_id}")
def atualizar(tarefa_id: int, tarefa_atualizada: TarefaUpdate):
    # Verifica se a tarefa existe antes de tentar atualizar
    if tarefa_id not in _tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    # Atualiza os campos mantendo o mesmo ID
    _tarefas[tarefa_id]["titulo"] = tarefa_atualizada.titulo
    _tarefas[tarefa_id]["concluida"] = tarefa_atualizada.concluida

    return _tarefas[tarefa_id]