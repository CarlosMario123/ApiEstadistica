from services.consumo.consumo import Consumo
from utils.groupArrayforDate import groupForAge

def checkFactibility():
    consumo = Consumo()
    data = consumo.get_consumed_agua()
    data = groupForAge(data,4)
    
    
    return data
    