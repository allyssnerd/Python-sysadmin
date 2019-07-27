import requests
nome = input('nome: ')
email = input('email: ')

usuario = {'nome': nome, 'email': email}

response = requests.post('http://192.168.205.144:8080/usuarios', json=usuario)


if response.status_code >= 200:
	response = response.json()
	print(response.get('mensagem'))

else:
	print('Nao foi dessa vez!')

print (usuario)

'''response = requests.get('http://192.168.205.144:8080/usuarios')

listar = requests.json()

for user in listar:
	print('Nome {0} e E-mail {1}'.format(user['nome'], user['email']))'''