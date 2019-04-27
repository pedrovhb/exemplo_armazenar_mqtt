import time
import random

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Conectado com resultado " + str(rc))


# Criamos o cliente MQTT e nos conectamos ao broker em rede local
client = mqtt.Client()
client.on_connect = on_connect

client.connect("localhost", 1883, 60)

# Começamos com um valor de temperatura de 25 graus.
# A cada 5 segundos, atualizamos esse valor, somando um número aleatório entre -1 e 1.
# Depois de modificar a temperatura simulada, publicamos a nova temperatura no tópico "valores/temperatura".

valor_temperatura = 25
while True:
    valor_temperatura += random.uniform(-1, 1)
    print(f'Publicando valor aleatório de temperatura {round(valor_temperatura, 2)}...')
    client.publish('valores/temperatura', valor_temperatura)
    time.sleep(5)
