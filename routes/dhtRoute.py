import numpy as np
import pandas as pd
from flask import Blueprint, jsonify
from statsmodels.tsa.arima.model import ARIMA


dhtRoute = Blueprint("dht", __name__, url_prefix='/dht')


@dhtRoute.route("/hour", methods=["GET"])
def inicio():
    datos_temperatura = leer_datos_dht11()
    
    # Si hay menos de 120 datos, completar con el último valor conocido
    if len(datos_temperatura) < 120:
        datos_temperatura.extend([datos_temperatura[-1]] * (120 - len(datos_temperatura)))
    
    # Crear una serie temporal
    serie_temperatura = pd.Series(datos_temperatura)

    # Ajustar el modelo ARIMA
    model = ARIMA(serie_temperatura, order=(5, 1, 0))  # (p,d,q) parámetros del modelo ARIMA
    model_fit = model.fit()

    # Hacer la predicción para la próxima hora (120 lecturas, cada 30 segundos)
    prediccion = model_fit.forecast(steps=120)

    # Formatear la predicción para la respuesta JSON
    prediccion_lista = prediccion.tolist()
    
    media = np.mean(prediccion_lista)
    respuesta = {
        "prediccion_proxima_hora": media
    }

    return jsonify(respuesta)

def leer_datos_dht11():#usos de simulacion 
    
    return np.random.normal(24, 1, 60).tolist()


