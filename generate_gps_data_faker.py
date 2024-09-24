from faker import Faker
import time
import random
import json
from decimal import Decimal

fake = Faker()

def generate_gps_data(bus_id, num_records):
    gps_data = []
    for _ in range(num_records):
        record = {
            "id": bus_id,
            "latitud": fake.latitude(),
            "longitud": fake.longitude(),
            "timestamp": int(time.time()),
            "speed": round(random.uniform(0, 80), 2)  # Convertir a float
        }
        gps_data.append(record)
        time.sleep(1)  # Simula una actualización por segundo
    return gps_data

# Generar datos para 3 autobuses durante 10 registros
num_records = 10
buses = ["bus_1", "bus_2", "bus_3"]

# Codificador personalizado para serializar Decimal a float
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)
    
for bus in buses:
    data = generate_gps_data(bus, num_records)
    print(json.dumps(data, indent=4, cls=DecimalEncoder))