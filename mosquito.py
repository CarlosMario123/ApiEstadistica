import paho.mqtt.client as mqtt
import numpy as np

# Configuración del cliente MQTT
mqtt_broker = "practicaspoli.zapto.org"  # Dirección del broker MQTT
mqtt_port = 1883                        # Puerto del broker MQTT
mqtt_topic_sub = "/suscribcion"         # Tópico al que te suscribes
mqtt_topic_pub = "/publicacion"         # Tópico al que publicas los mensajes reenviados

# Credenciales de autenticación
mqtt_username = "rasp"                  # Usuario MQTT
mqtt_password = "1234"                  # Clave MQTT

# Función que se ejecuta cuando el cliente se conecta al broker
def on_connect(client, userdata, flags, rc):
    print("Conectado al broker con código de resultado " + str(rc))
    # Suscribirse al tópico
    client.subscribe(mqtt_topic_sub)

# Función que se ejecuta cuando se recibe un mensaje
def on_message(client, userdata, msg):
    print(f"Mensaje recibido en {msg.topic}: {msg.payload.decode()}")
    if msg.topic == mqtt_topic_sub:
        data = np.random.normal(24, 1, 60).tolist()
        data_str = ','.join(map(str, data))
        print(data_str)
        client.publish(mqtt_topic_pub, data_str)

# Crear instancia del cliente MQTT
client = mqtt.Client()

# Asignar funciones de manejo de eventos
client.on_connect = on_connect
client.on_message = on_message

# Configurar autenticación
client.username_pw_set(mqtt_username, mqtt_password)

# Conectar al broker MQTT
client.connect(mqtt_broker, mqtt_port, 60)

# Mantener el cliente en ejecución
client.loop_forever()
