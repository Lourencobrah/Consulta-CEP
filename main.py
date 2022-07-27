import pandas as pd
import openpyxl
import json
import requests

num_cep = int(input('Digite o CEP: '))

cep = requests.get('https://viacep.com.br/ws/'+str(num_cep)+'/json/')

cep = cep.json()

print('CEP: ' + cep['cep'] + "\nLOGRADOURO: " + cep['logradouro'] + "\nCOMPLEMENTO: " + cep['complemento'] + "\nBAIRRO: " + cep['bairro'] + "\nLOCALIDADE: " + cep['localidade'] + "\nUF: " + cep['uf'] + "\nIBGE: " + cep['ibge'] + "\nGIA: " + cep['gia'] + "\nDDD: " + cep['ddd'] + "\nSIAFI: " + cep['siafi'])