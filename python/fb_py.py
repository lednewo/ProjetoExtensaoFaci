
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import uuid
from dataclasses import *

#Definindo as credenciais do Firebase
# cred = credentials.Certificate("#")

#Checando se a seção está online
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

#Criando o cliente
db = firestore.client()

Cards = [{
     'Comprador' : 'Eu',
     'Origem' : '',
     'Destino' : '',
     'Data' : '',
     'Num_animais' : '',
     'ID': str(uuid.uuid4())
}]

#Cards.append({"Comprador": "Nulo", "ID": str(uuid.uuid4())})

# ADICIONAR LISTA PARA JSON

def jsonAdicionarLista(lista: list):
  jsonDicionarios = json.dumps(lista, indent = 4) #converte lista em um json
  #print(jsonDicionarios)
  return jsonDicionarios

# ADICIONAR JSON PARA FIREBASE

def fbAdicionarJson(jsonCards: json):
  jsonLista = json.loads(jsonCards) #converte json para uma lista
  for index, dicionario in enumerate(jsonLista):
    db.collection("Cards").document(dicionario.get('ID')).set(jsonLista[index])

# BAIXAR DO FIREBASE PARA JSON

def jsonBaixarFB():
  teste = [] #alterar
  campos_desejados = ['Comprador', 'Origem', 'Destino', 'Data', 'Num_animais', 'ID']
  for doc in db.collection("Cards").stream():
      dados_ordenados = {campo: doc.to_dict().get(campo) for campo in campos_desejados if campo in doc.to_dict()}
      teste.append(dados_ordenados)
  return json.dumps(teste, indent = 4)

# ADICIONAR JSON PARA LISTA

def listaAdicionarJson(jsonCards: json, lista: list ):
  lista = json.loads(jsonCards, indent = 4)
  return lista

# ALTERAR CAMPOS

def alterar_comprador(lista: list, novocomprador: str, i: int):
  lista[i]['Comprador'] = novocomprador
  jsonCards = jsonAdicionarLista(lista)
  fbAdicionarJson(jsonCards)

def alterar_origem(lista: list, novaorigem: str, i: int):
  lista[i]['Origem'] = novaorigem
  jsonCards = jsonAdicionarLista(lista)
  fbAdicionarJson(jsonCards)

def alterar_destino(lista: list, novodestino: str, i: int):
  lista[i]['Destino'] = novodestino
  jsonCards = jsonAdicionarLista(lista)
  fbAdicionarJson(jsonCards)

def alterar_data(lista: list, novadata: str, i: int):
  lista[i]['Data'] = novadata
  jsonCards = jsonAdicionarLista(lista)
  fbAdicionarJson(jsonCards)

def alterar_num_animais(lista: list, novonum_animais: int, i: int):
  lista[i]['Num_animais'] = novonum_animais
  jsonCards = jsonAdicionarLista(lista)
  fbAdicionarJson(jsonCards)
