from datetime import datetime

from modelo_banco import criar_sessao, ValorTemperatura
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Conectado com resultado " + str(rc))


def on_message(client, userdata, msg):
    # Se o tópico for o nosso tópico de temperatura...
    if msg.topic == 'valores/temperatura':

        valor_temperatura = float(msg.payload)
        print(f'Recebido valor de temperatura {valor_temperatura}')

        # Criamos um objeto ValorTemperatura
        novo_valor = ValorTemperatura(
            temperatura=valor_temperatura,
            criacao=datetime.now())

        # Criamos uma sessão de conexão com o banco de dados, inserimos o novo objeto,
        # fazemos o commit e fechamos a sessão
        sessao = criar_sessao()
        sessao.add(novo_valor)
        sessao.commit()
        sessao.close()
    else:
        # Nesse caso, o tópico não é o de temperatura; só printamos a mensagem
        print(f'[{msg.topic}] {msg.payload}')


# Criamos o cliente MQTT e definimos o callback a ser usado pra mensagem e conexão
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Nos conectamos ao broker MQTT. Nesse caso, ele está na máquina local.
client.connect("localhost", 1883, 60)

# Nos inscrevemos em todos os tópicos que comecem com "valores/".
# Daqui vão vir nossos valores de temperatura.
client.subscribe('valores/#')

# Ficamos aguardando mensagens pra sempre.
# O fluxo do programa se dá quando chega uma mensagem e a função
# on_message é executada com os dados da mensagem que chegou.
client.loop_forever()
