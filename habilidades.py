from flask import request
from flask_restful import Resource
import json

lista_habilidades = ['python', 'Java', 'Flask', 'PHP', 'Django']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        if not dados['habilidade'] in lista_habilidades:
            lista_habilidades.append(dados['habilidade'])
            status = 'sucesso'
            msg = 'Registro incluído'
        else:
            status = 'erro'
            msg = 'Valor informado já está presenta na lista'
        return {'status': status, 'msg': msg}

class HabilidadesId(Resource):
    def put(self,id):
        try:
            dados = json.loads(request.data)
            lista_habilidades[id]=dados['habilidade']
            status = 'sucesso'
            msg = 'Registro {} alterado'.format(id)
        except IndexError:
            status = 'erro'
            msg = 'Registro {} não existe'.format(id)
        except Exception:
            status = 'erro'
            msg = 'Erro desconhecido, contato do desenvolvedor da API'
        return {'status': status, 'msg': msg}

    def delete(self,id):
        try:
            lista_habilidades.pop(id)
            status = 'sucesso'
            msg = 'Registro {} excluido'.format(id)
        except IndexError:
            status = 'erro'
            msg = 'Registro {} não existe'.format(id)
        except Exception:
            status = 'erro'
            msg = 'Erro desconhecido, contato do desenvolvedor da API'
        return {'status': status, 'msg': msg}


