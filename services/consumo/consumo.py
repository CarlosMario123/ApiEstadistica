from bd.BD import BD
from datetime import datetime

class Consumo:
    def __init__(self):
        self.bd = BD()

    def get_consumed(self,option="water"):
        value = "Consumo_de_agua"
        if option == "food":
            value = "Consumo_de_alimento"
            
        try:
            connection = self.bd.get_connection()
            cursor = connection.cursor()
            query = f"SELECT * FROM {value};"
            cursor.execute(query)
            results = cursor.fetchall()
            formatted_data = [(day, value, date.date()) for day, value, date in results]
            return formatted_data
        
        except Exception as e:
            print(f"Error al obtener los datos: {e}")
            return None
        finally:
           
            if cursor:
                cursor.close()
            if connection:
                connection.close()
                


