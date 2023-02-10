import json
from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, HabilidadesId

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': '0', 'nome': 'Carlos', 'habilidades': ['Python', 'Flask']},
    {'id': '1', 'nome': 'Stella', 'habilidades': ['Python', 'Django']}

]


class Desenvolvedor(Resource):
    def get(self, id): # Retorna um desenvolvedor numa determinada posiçao id
            try:
                response = desenvolvedores[id]
            except IndexError:
                response = {'status': 'erro', 'mensagem': f'Desenvolvedor de ID {id} nao existe'}
            except Exception:
                mensagem = 'Erro desconhecido. Procure o administrador da API'
                response = {'status': 'erro', 'mensagem': mensagem}
            return response

    def put(self, id): # Altera os dados de um desenvolvedor numa determinada posiçao id
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id): # Deleta um desenvolvedor numa determinada posiçao id
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class ListaDesenvolvedores(Resource):
    def get(self): # Lista todos os desenvolvedores
        return desenvolvedores

    def post(self): # Cria um desenvolvedor a partir dos dados informados e insere automaticamente uma id
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev')
api.add_resource(Habilidades, '/habilidades')
api.add_resource(HabilidadesId, '/habilidades/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
