from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = FastAPI()

@app.post("/embrapa_producao/")
def extracao_producao_ano(ano):
    response = requests.get('http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao={opcao}')

    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {'class': 'tb_base tb_dados'})

    products = []
    quantities = []

    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) > 1:  
            product = columns[0].get_text(strip=True)
            quantity = columns[1].get_text(strip=True)
            products.append(product)
            quantities.append(quantity)

    df = pd.DataFrame({
        'Produto': products,
        'Quantidade (L.)': quantities
    })

    return {"message": df.to_dict("records")}