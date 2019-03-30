import requests
import json

url = 'http://data.fixer.io/api/latest?access_key=6647d025843f40aafdfba3c855e69bd2'

print('Acessando Base de Dados...')
response = requests.get(url)
if response.status_code == 200:
	print('Base de Dados Acessada!')
	print('Buscando Informações das Moedas...')
	dados = response.json() 
	euro_real = dados['rates']['BRL'] / dados['rates']['EUR']
	dollar_real = dados['rates']['BRL'] / dados['rates']['USD']
	btc_real = dados['rates']['BRL'] / dados['rates']['BTC']
	print('%.2f' % euro_real)
	print('%.2f' % dollar_real)
	print('%.2f' % btc_real)


else:
	print('Erro no Site!')