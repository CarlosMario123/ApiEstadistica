from bd.BD import BD
from datetime import datetime, timedelta
import random
bd = BD()
conn = bd.get_connection()
cursor = conn.cursor()

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 7, 5)
num_days = (end_date - start_date).days

for _ in range(num_days + 1):  # Incluyendo el día final
    current_datetime = start_date + timedelta(days=_)
    cantidad = round(random.uniform(350, 320), 2)  # Generar un número aleatorio entre 350 y 400 con 2 decimales
    cursor.execute('''
    INSERT INTO Consumo_de_alimento (fecha, cantidad) VALUES (%s, %s)
    ''', (current_datetime.strftime('%Y-%m-%d %H:%M:%S'), cantidad))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print(f"Se han insertado datos falsos desde {start_date.strftime('%Y-%m-%d')} hasta {end_date.strftime('%Y-%m-%d')}")