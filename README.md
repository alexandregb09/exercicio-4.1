# Exercício 4.1 — API REST de uma aplicação de TODO list (POST/GET/PUT)

**Aluno:** *Alexandre Garcia Bezerra*
**Disciplina:** IDP-TD 2026
**Framework usado:** *FastAPI + Uvicorn*

\---

## O que esta API faz

API REST que serve de **backend de uma aplicação de TODO list** — gerencia
**tarefas** (`{id, titulo, concluida}`), com armazenamento em memória, rodando em
`http://localhost:8000`. Implementa POST (criar), GET (ler) e
PUT (atualizar), seguindo o contrato do [tutorial\_4.1.md](tutorial_4.1.md#3-contrato-da-api-obrigatório--o-autograder-depende-disto).

## Estrutura

* [app/main.py](app/main.py) — implementação da API
* [requirements.txt](requirements.txt) — dependências (`fastapi`, `uvicorn`)
* [`.autograde-exercise`](.autograde-exercise) — marcador do autograder (conteúdo: `4.1`)

## Como rodar

```bash
pip install -r requirements.txt
uvicorn app.main:app --port 8000
```

## Como validar

Com a API rodando (recém-reiniciada, store vazio), em outro terminal dentro do repo:

```bash
autograde validar 4.1
```

## Endpoints

|Método|Rota|Descrição|
|-|-|-|
|GET|`/health`|liveness — `{"status":"ok"}`|
|POST|`/tarefas`|cria tarefa a partir de `{"titulo": "..."}`|
|GET|`/tarefas/{id}`|lê uma tarefa (404 se não existe)|
|GET|`/tarefas`|lista todas|
|PUT|`/tarefas/{id}`|atualiza `titulo` e `concluida`|

## Decisões de implementação

### Escolha do Framework

Optou-se pelo **FastAPI** devido à sua alta performance, tipagem estática nativa baseada em Type Hints do Python e validação de dados automática em tempo de execução via Pydantic. Essas características mitigam erros comuns de tipagem e aceleram o cumprimento exato do contrato técnico determinado pelo exercício.

### Modelagem do Store

O armazenamento das tarefas foi estruturado utilizando um dicionário nativo do Python (`dict[int, dict]`) associado a uma variável global de controle de índice incremental (`_proximo_id = 1`). Essa abordagem cumpre o requisito de volatilidade (zerar o estado ao reiniciar a aplicação) e garante busca em tempo constante O(1) por ID.

### Tratamento de 404

Para os endpoints `GET /tarefas/{id}` e `PUT /tarefas/{id}`, o sistema verifica previamente se a chave existe no dicionário. Caso o ID não seja encontrado, dispara `HTTPException(status_code=404, detail="Tarefa não encontrada")`, respeitando as convenções REST.



