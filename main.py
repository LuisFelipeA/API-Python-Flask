import pandas as pd

tabela = pd.read_csv('Base de Dados.csv')

total_vendas = tabela['Vendas'].sum()

print(tabela)

print(total_vendas)
