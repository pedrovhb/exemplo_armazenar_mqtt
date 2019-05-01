# Exemplo de armazenamento de dados MQTT

Esse repositório mostra o armazenamento de dados vindos de um broker MQTT, protocolo de comunicação especializado em 
aplicações da Internet das Coisas. Foi feito pra disponibilizar o código relevante [a esse post no meu 
blog](https://pedrovhb.com/aquisicao-de-dados-via-mqtt-e-armazenamento-em-banco-de-dados-relacional/)!

![Diagrama](https://github.com/pedrovhb/exemplo_armazenar_mqtt/raw/master/images/DiagramaArmazenamentoMQTT.png)

## Overview

Vamos criar um gerador de dados de temperatura simulado (pra servir como nosso sensor), modelar um banco de dados em 
SQLAlchemy e criar um cliente MQTT que se inscreva nos tópicos que contém os dados simulados, armazenando esses dados
no banco criado.

Por fim, criamos uma pequena aplicação Flask que interage com o banco de dados criado e disponibiliza de front-end
uma página da web simples com um gráfico que se atualiza em tempo real:

![Front-end com gráfico](https://github.com/pedrovhb/exemplo_armazenar_mqtt/raw/master/images/InterfaceWeb.png)
