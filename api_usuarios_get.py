import requests
import sys

buscar = sys.argv
if len(buscar) > 1:
	response = requests.get('http://192.168.205.144:8080/usuarios?nome={}'.format(buscar[1]))

else:
	response = requests.get('http://192.168.205.144:8080/usuarios')

listen_user = response.json()

for iden in listen_user:
	print('{} - {}'.format(iden['_id'], iden['nome']))
#print(response.text)

nome = input('Digite o nome: ')
response = requests.get('http://192.168.205.144:8080/usuarios?=nome{0}'.format(nome))

listen_user = response.json()

for iden in listen_user:
	print('{} - {}'.format(iden['_id'], iden['nome']))
#print(response.text)


#outra maneira
'''nome = input('Digite o nome: ')
response = requests.get('http://192.168.205.144:8080/usuarios?=nome{0}'.format(nome))

listen_user = response.json()

for iden in listen_user:
	print('{} - {}'.format(iden['_id'], iden['nome']))
#print(response.text)'''