from fastapi import FastAPI, Query
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import Optional, List, Dict, Any

app = FastAPI()

class QueryParams(BaseModel):
    ano: Optional[int] = Query(None, description="Ano para filtrar os dados")
    opcao: str = Query(..., description="Opção principal para a URL")
    subopcao: Optional[str] = Query(None, description="Subopção para filtrar os dados")

def parse_table(table) -> List[Dict[str, Any]]:
    data = []
    current_category = None
    current_subcategory = None

    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) == 1:
            # This is a category or subcategory row
            text = columns[0].get_text(strip=True)
            if text.isupper():
                current_category = text
                current_subcategory = None
            else:
                current_subcategory = text
        elif len(columns) > 1:
            # This is a data row
            product = columns[0].get_text(strip=True)
            quantity = columns[1].get_text(strip=True)
            entry = {
                "Produto": product,
                "Quantidade (L.)": quantity,
            }
            if current_subcategory:
                entry["Subcategoria"] = current_subcategory
            if current_category:
                entry["Categoria"] = current_category
            data.append(entry)
    return data

@app.post("/embrapa_producao/")
def extracao_producao(params: QueryParams):
    base_url = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
    
    # Construindo a URL com os parâmetros fornecidos
    query_params = {
        "opcao": params.opcao,
    }
    if params.ano:
        query_params["ano"] = params.ano
    if params.subopcao:
        query_params["subopcao"] = params.subopcao
    
    response = requests.get(base_url, params=query_params)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'tb_base tb_dados'})
    
    if table is None:
        return {"message": "No data found for the given parameters"}
    
    data = parse_table(table)
    
    return {"message": data}
