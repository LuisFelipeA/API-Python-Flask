import requests

link = 'http://127.0.0.1:5000/totalvendas'

requisicao =  requests.get(link)

#Retorna o status da Requisição. Ex: 200 (deu certo)
#print(requisicao)

#Retorna o conteudo da requisição
#print(requisicao.json())

total_vendas = requisicao.json()

print(f"Total de Vendas: R${total_vendas['total_vendas']:.2f}")