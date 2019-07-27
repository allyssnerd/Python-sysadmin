import requests

id_user = input('Informe o ID: ')

response = requests.delete('http://192.168.205.144:8080/usuarios/{}'.format(int(id_user)))
print(response.json())