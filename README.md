# Embrapa Data Extraction API

## Descrição
API para extração de dados de produção e processamento da Embrapa, construída com FastAPI.

## Estrutura do Projeto
fiap-tech-challenge-1/ <br />
├── .gitignore <br />
├── README.md <br />
├── requirements.txt <br />
└── requests_embrapa_api.py <br />


## Instruções de Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/rrbcode/fiap-tech-challenge-1.git
   
2. Navegue até o diretório do projeto:
   ```bash
   cd fiap-tech-challenge-1

3. Crie um ambiente virtual e ative-o:
   ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`

4. Instale as dependências:
   ```bash
    pip install -r requirements.txt

## Executando a API Localmente

1. Execute a API:
   ```bash
    uvicorn requests_embrapa_api:app --reload

2. Acesse a documentação interativa em: <br />
   Swagger UI: http://localhost:8000/docs <br />
   Redoc: http://localhost:8000/redoc <br />

## Endpoints Disponíveis

### Produção
- GET /embrapa_producao/
   - Descrição: Extrai dados de produção da Embrapa para os anos especificados.
   - Exemplo de resposta:
   ```json
   {
  "message": [
       {
      "id_name": "some_value",
      "control": "some_value",
      "produto": "some_value",
      "1970": "some_value",
      ...
      "2023": "some_value"
       },
       ...
     ]
   }

### Processamento
- POST /embrapa_processamento/
   - Descrição: Extrai dados de processamento da Embrapa para um tipo de processamento especificado.
   - Parâmetros:
     - processamento (obrigatório): Tipo de processamento para filtrar os dados.
   - Exemplo de corpo da requisição:
      ```json
      {
        "processamento": "some_process_type"
      }
   - Exemplo de resposta:
      ```json
      {
        "message": [
          {
            "control": "some_value",
            "cultivar": "some_value",
            "1970": "some_value",
            ...
            "2022": "some_value"
          },
          ...
        ]
      }

## Deploy

1. Suba o projeto para o GitHub.
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/seu-usuario/fiap-tech-challenge-1.git
   git push -u origin master

2. Crie o serviço de hospedagem no Render (ou outro serviço de sua escolha).
- Configure o repositório GitHub no serviço de hospedagem.
- Defina o comando de inicialização:
  ```bash
   uvicorn requests_embrapa_api:app --host 0.0.0.0 --port 8000

## Links Úteis

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [Pandas](https://pandas.pydata.org/)
