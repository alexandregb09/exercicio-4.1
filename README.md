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

Decisões de ImplementaçãoEscolha do FrameworkOptou-se pelo FastAPI devido à sua alta performance, tipagem estática nativa baseada em Type Hints do Python e validação de dados automática em tempo de execução via Pydantic. Essas características mitigam erros comuns de tipagem (como o recebimento de valores booleanos disfarçados de strings de texto) e aceleram o cumprimento exato do contrato técnico determinado pelo exercício.Modelagem do Repositório de Dados (Data Store)O armazenamento das tarefas foi estruturado utilizando um dicionário nativo do Python (dict\[int, dict]) associado a uma variável global de controle de índice incremental (\_proximo\_id = 1). Essa abordagem cumpre perfeitamente o requisito de volatilidade (zerar o estado ao reiniciar a aplicação) e garante uma complexidade de busca de tempo constante $O(1)$ ao recuperar ou atualizar registros por meio de sua chave primária (id).Tratamento de Erros e Casos de Borda (404)Para os endpoints de consulta individual (GET /tarefas/{id}) e modificação (PUT /tarefas/{id}), o sistema realiza uma verificação prévia de associação de chave dentro do dicionário global. Caso o identificador fornecido pelo cliente não seja encontrado no mapa de dados, a API interrompe o fluxo imediatamente disparando uma exceção do tipo HTTPException(status\_code=404, detail="Tarefa não encontrada"). Isso garante que o código de status HTTP correto (404) seja despachado para o cliente, respeitando as convenções da arquitetura REST."""with open("README.md", "w", encoding="utf-8") as f:f.write(readme\_content)print("README.md gerado com sucesso!")

```text?code\_stdout\&code\_event\_index=1



