import pandas as pd
from datasynthesizer import DataSynthesizer
from datasynthesizer.synthesizers import GaussianMixtureSynthesizer

# Leer datos reales desde un archivo CSV
real_data = pd.read_csv('real_gps_data.csv')

# Configurar el sintetizador
synthesizer = GaussianMixtureSynthesizer()

# Ajustar el sintetizador a los datos reales
synthesizer.fit(real_data)

# Generar datos sintéticos
num_synthetic_records = 10
synthetic_data = synthesizer.sample(num_synthetic_records)

# Guardar datos sintéticos en un archivo CSV
synthetic_data.to_csv('synthetic_gps_data.csv', index=False)

print(synthetic_data)