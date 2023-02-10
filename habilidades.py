from flask_restful import Resource
from flask import request
import json

lista_habilidades = ['Python', 'Java', 'PHP']

class Habilidades(Resource):
    def get(self):  # Retorna tudo
        return lista_habilidades

    def post(self):  # Insere uma nova habilidade na lista
        dados = json.loads(request.data)
        lista_habilidades.append(dados.get('Habilidade'))
        return lista_habilidades


class HabilidadesId(Resource):
    def put(self, id):  # Altera a habilidade numa determinada posiçao id informada na URI
        dados = json.loads(request.data)
        lista_habilidades[id]= (dados.get('Habilidade'))
        return lista_habilidades

    def delete(self, id):  # Deleta a habilidade numa determinada posição id informada na URI
        lista_habilidades.pop(id)
        return lista_habilidades
