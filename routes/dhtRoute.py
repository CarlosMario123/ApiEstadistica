import numpy as np
import pandas as pd
from flask import Blueprint, jsonify
from statsmodels.tsa.arima.model import ARIMA
import paho.mqtt.client as mqtt
import time

dhtRoute = Blueprint("dht", __name__, url_prefix='/dht')

mqtt_broker = "practicaspoli.zapto.org"  # Dirección del broker MQTT
mqtt_port = 1883                        # Puerto del broker MQTT
mqtt_topic_request = "/suscribcion"     # Tópico para solicitar datos
mqtt_topic_response = "/publicacion"    # Tópico para recibir datos
mqtt_username = "rasp"                  # Usuario MQTT
mqtt_password = "1234"                  # Clave MQTT

received_data = None

def on_connect(client, userdata, flags, rc):
    print("Conectado al broker con código de resultado " + str(rc))
    client.subscribe(mqtt_topic_response)

def on_message(client, userdata, msg):
    global received_data
    received_data = msg.payload.decode()

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.username_pw_set(mqtt_username, mqtt_password)
mqtt_client.connect(mqtt_broker, mqtt_port, 60)
mqtt_client.loop_start()  # Iniciar el loop en segundo plano

@dhtRoute.route("/hour", methods=["GET"])
def inicio():
    datos_temperatura = leer_datos_dht11()

    if isinstance(datos_temperatura, str):
        return jsonify({"Error": datos_temperatura})

    if len(datos_temperatura) < 120:
        datos_temperatura.extend([datos_temperatura[-1]] * (120 - len(datos_temperatura)))

    serie_temperatura = pd.Series(datos_temperatura)

    try:
        model = ARIMA(serie_temperatura, order=(5, 1, 0))
        model_fit = model.fit()

        prediccion = model_fit.forecast(steps=120)

        prediccion_lista = prediccion.tolist()
        media = np.mean(prediccion_lista)
        respuesta = {
            "prediccion_proxima_hora": media
        }
        return jsonify(respuesta)
    
    except Exception as e:
        return jsonify({"Error": str(e)})

def leer_datos_dht11():
    global received_data
    received_data = None

    mqtt_client.publish(mqtt_topic_request, "solicitar_datos")

    timeout = time.time() + 5  # Esperar hasta 5 segundos por la respuesta
    while received_data is None and time.time() < timeout:
        time.sleep(0.1)

    if received_data is None:
        return "Lo sentimos, los datos no se pudieron obtener. Intente de nuevo más tarde."

    try:
        datos = list(map(float, received_data.split(',')))
        return datos
    except ValueError:
        return "Error al procesar los datos recibidos. Por favor, inténtelo nuevamente."
