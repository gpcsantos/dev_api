from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, HabilidadesId
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id':'0',
        'nome':'Glauco',
        'habilidades':['Python','Flask']
     },
    {
        'id':'1',
        'nome':'Santos',
        'habilidades':['Python','Django','MySql','PHP','C#']
     }
]

# Devolve um desenvolvedor pelo ID. Também altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]  # id relativo à posição no dicionário
        except IndexError:
            status = 'erro'
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': status, 'mensagem': mensagem}
        except Exception:
            status = 'erro'
            mensagem = 'Erro desconhecido. Procure o Adinistrador da API.'
            response = {'status': status, 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        status = 'sucesso'
        mensagem = 'Registro ID {} excluído'.format(id)
        response = {'status': status, 'mensagem': mensagem}
        return response

#Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

    def get(self):
        return desenvolvedores

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores,'/dev/' )
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(HabilidadesId, '/habilidades/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)