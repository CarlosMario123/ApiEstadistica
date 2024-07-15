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
    """Callback para cuando el cliente MQTT se conecta."""
    if rc == 0:
        print("Conectado al broker MQTT con éxito.")
        client.subscribe(mqtt_topic_response)
    else:
        print(f"Fallo al conectar al broker MQTT. Código de retorno={rc}")

def on_message(client, userdata, msg):
    """Callback para cuando se recibe un mensaje MQTT."""
    global received_data
    received_data = msg.payload.decode()

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.username_pw_set(mqtt_username, mqtt_password)

try:
    mqtt_client.connect(mqtt_broker, mqtt_port, 60)
    mqtt_client.loop_start()  # Iniciar el loop en segundo plano
except ConnectionRefusedError:
    print("No se puede conectar al broker MQTT. Verifique la configuración.")

@dhtRoute.route("/hour", methods=["GET"])
def inicio():
    """Endpoint para obtener la predicción de temperatura para las próximas 6 horas."""
    datos_temperatura = leer_datos_dht11()

    if isinstance(datos_temperatura, str):
        return jsonify({"Error": datos_temperatura})

    serie_temperatura = pd.Series(datos_temperatura)

    try:
        # Ajustar el modelo ARIMA con parámetros optimizados según análisis previo
        model = ARIMA(serie_temperatura, order=(5, 1, 0))
        model_fit = model.fit()

        # Realizar la predicción para las próximas 6 horas (12 pasos)
        prediccion = model_fit.forecast(steps=12)

        # Calcular la media de la predicción
        media_prediccion = np.mean(prediccion)

        # Preparar la respuesta JSON con la predicción media
        respuesta = {
            "prediccion_proximas_6_horas": media_prediccion
        }
        return jsonify(respuesta)
    
    except Exception as e:
        return jsonify({"Error": f"Error en el modelo ARIMA: {str(e)}"})

def leer_datos_dht11():
    """Función para leer los datos de temperatura desde el sensor DHT11 a través de MQTT."""
    global received_data
    received_data = None

    try:
        # Publicar solicitud para obtener datos del sensor DHT11
        mqtt_client.publish(mqtt_topic_request, "solicitar_datos")

        # Esperar hasta 5 segundos para recibir la respuesta del sensor
        timeout = time.time() + 5
        while received_data is None and time.time() < timeout:
            time.sleep(0.1)

        if received_data is None:
            return "Error: No se recibieron datos del sensor DHT11."

        # Convertir los datos recibidos a una lista de números (temperaturas)
        datos = list(map(float, received_data.split(',')))
        return datos
    
    except Exception as e:
        return f"Error en la lectura de datos del sensor DHT11: {str(e)}"
