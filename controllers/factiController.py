from services.consumo.consumo import Consumo
from utils.groupArrayforDate import groupForAge

def checkFactibility():
    consumo = Consumo()
    data = consumo.get_consumed()
    data = groupForAge(data,4)
    
    
    return data

def checkFactFood():
    consumo = Consumo()
    data = consumo.get_consumed(option="food")
    data = groupForAge(data,4)
    return data