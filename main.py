import pandas as pd
from flask import Flask,jsonify

# Inicializando aplicação
app = Flask(__name__)

#Define Rota da Pagina Inicial
@app.route('/') 
# Função que retorna Informações da rota chamada

def homepage():
    return 'API Funcionando'


 #Define Rota Personalizada
@app.route('/totalvendas')

def totalVendas():
    # Importando Base de Dados e Somando Vendas
    tabela = pd.read_csv('Base de Dados.csv')
    total_vendas = tabela['Vendas'].sum()

    resposta = {'total_vendas': total_vendas}

    return jsonify(resposta)



# Rodar API
app.run(host='0.0.0.0')