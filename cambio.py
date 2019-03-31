import pandas as pd
import requests
import json
import decimal

url = 'http://data.fixer.io/api/latest?access_key=6647d025843f40aafdfba3c855e69bd2'

print('Acessando Base de Dados...')
response = requests.get(url)
if response.status_code == 200:
	print('Base de Dados Acessada!')
	print('Buscando Informações das Moedas...')
	dados = response.json() 
	day = dados['date']
	print('Acessando dados do dia: %s/%s/%s' % (day[8:], day[5:7], day[0:4]))
	euro_real = round(dados['rates']['BRL'] / dados['rates']['EUR'], 2)
	dollar_real = round(dados['rates']['BRL'] / dados['rates']['USD'], 2)
	btc_real = round(dados['rates']['BRL'] / dados['rates']['BTC'], 2)
	print('Euro: %.2f' % euro_real)
	print('Dollar: %.2f' % dollar_real)
	print('Bitcoin: %.2f' % btc_real)
	df = pd.DataFrame({'Moedas': ['Euro', 'Dollar', 'Real'], 'Valores':[euro_real, dollar_real, btc_real]})
	df.to_csv('valores.csv', index=False, sep=';')

else:
	print('Erro no Site!')
