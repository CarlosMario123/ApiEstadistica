from services.consumo.consumo import Consumo
from utils.groupArrayforDate import groupForAge

def checkFactibility():
    consumo = Consumo()
    data = consumo.get_consumed()
    data = groupForAge(data,4)
    send = {}
    for d in data:
        if data[d] > 0:
            send[d] = data[d]
   
    return send

def checkFactFood():
    consumo = Consumo()
    data = consumo.get_consumed(option="food")
    data = groupForAge(data,4)
    send = {}
    for d in data:
        if data[d] > 0:
            send[d] = data[d]
   
    return send