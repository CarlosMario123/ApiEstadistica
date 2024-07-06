from datetime import datetime

def groupForAge(data,group):
    
    if not (group == 2 or group == 3 or group == 4 or  group == 6):
        return "No se puede agrupar de esa manera"
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    
    fecha = {
    'Jan': 0,
    'Feb': 0,
    'Mar': 0,
    'Apr': 0,
    'May': 0,
    'Jun': 0,
    'Jul': 0,
    'Aug': 0,
    'Sep': 0,
    'Oct': 0,
    'Nov': 0,
    'Dec': 0
           }
    
    
    for i in data:
        fecha[i[2].strftime('%b') ] =  fecha[i[2].strftime('%b') ] + i[1]
    
   

    limit = 12 / group
    group = {}
    fecha2 = ""
    i = 1
    for g in meses:
        
        if i == 1:
            fecha2 = g
        
        if i == limit:
            fecha2 = fecha2 + "-" + g
            i = 0
            group[fecha2] = 0
            fecha2 = ""
        i += 1
    
    

    key = ""
    i = 1
    
    stackGroup = []
    for clave in group:
        stackGroup.append(clave)
 
    
    for mes, valor in fecha.items():
        
        if i == 1:
            key = stackGroup.pop(0)
             
                
                
        group[key] = group[key] + valor
       
        if i == limit:
    
            i = 0
        i += 1
            
        
        
 
    return group

    
    