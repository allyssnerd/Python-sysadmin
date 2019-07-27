
import requests
import sys

cep = sys.argv[1]
#cep = input ('CEP: ')

response = requests.get('http://viacep.com.br/ws/{}/json'.format(cep))

if response.status_code == 200:
	endereco = response.json()['logradouro']
	bairro = response.json()['bairro']
	print('Rua: {} - Bairro: {}'.format(endereco, bairro))

elif response.status_code == 400:
	print('Formato invalido')
	
else:
	print('Erro desconhecido')