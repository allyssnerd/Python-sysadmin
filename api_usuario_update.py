import requests

iden = input('Informe o ID: ')

response = requests.get('http://192.168.205.144:8080/usuarios')

listar = response.json()
dados = None

for user in listar:
	if user['_id'] == int(iden):
		dados = user

if dados is None:
	print('Usuario nao encontrado!')
	exit()

nome = input('Digite um novo nome: ')
email = input('Informe o E-mail: ')

usuario = {'nome': nome, 'email': email}

response = requests.put('http://192.168.205.144:8080/usuarios/{}'.format(iden), json=usuario)

print (response.json())
