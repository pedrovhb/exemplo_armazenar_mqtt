import json

from flask import Flask, render_template, jsonify
from modelo_banco import criar_sessao, ValorTemperatura

app = Flask(__name__)


@app.route('/')
def mostrar_dados():
    sessao = criar_sessao()
    # Aqui pegamos os dados que queremos mostrar na tela.
    # O que estamos fazendo é pedir os últimos 100 objetos
    # ValorTemperatura do nosso banco de dados.
    dados = sessao.query(ValorTemperatura).order_by(ValorTemperatura.criacao.desc()).limit(100).all()
    sessao.close()

    dados = list(reversed(dados))

    # Criamos listas separadas pra temperatura e pra datetime de criação dos dados.

    dados_temperatura = []
    for dado in dados:
        dados_temperatura.append(dado.temperatura)

    dados_criacao = []
    for dado in dados:
        # Aqui temos um objeto datetime, mas o Python não transforma isso em JSON automaticamente,
        # porque não é um formato padrão JSON. Ao invés disso, vamos transformar o valor de data de
        # criação em um timestamp.
        dados_criacao.append(dado.criacao.timestamp())

    # Retornamos o HTML já com os dados que queremos usar pro gráfico renderizados.
    return render_template('template.html',
                           dados_temperatura=json.dumps(dados_temperatura),
                           dados_criacao=json.dumps(dados_criacao))


# Essa função é chamada pelo JavaScript do nosso template.html,
# e serve pra atualizar a temperatura atual e adicionar um ponto ao gráfico.
@app.route('/update')
def update():
    sessao = criar_sessao()
    # Pegamos o ValorTemperatura mais recente pelo campo criacao
    ultima_atualizacao = sessao.query(ValorTemperatura).order_by(ValorTemperatura.criacao.desc()).first()
    sessao.close()

    dados_ultima_atualizacao = {'temperatura': ultima_atualizacao.temperatura,
                                'criacao': ultima_atualizacao.criacao.timestamp()}

    # Retornamos os dados em formato JSON
    return jsonify(dados_ultima_atualizacao)


if __name__ == '__main__':
    app.run()
