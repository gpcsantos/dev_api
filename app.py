from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id] # id relativo à posição no dicionário
        except IndexError:
            status = 'erro'
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':status,'mensagem':mensagem}
        except Exception:
            status = 'erro'
            mensagem = 'Erro desconhecido. Procure o Adinistrador da API.'
            response = {'status': status, 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        status = 'sucesso'
        mensagem = 'Registro excluído'
        response = {'status': status, 'mensagem': mensagem}
        return jsonify(response)


#Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)