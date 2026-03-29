from prometheus_client import start_http_server, Gauge
import time
import random # Aquí irían tus funciones reales de red o crypto

# Definimos las métricas para Nexus
NETWORK_TRAFFIC = Gauge('nexus_network_activity', 'Actividad de red detectada')
CRYPTO_PRICE = Gauge('nexus_binance_btc_price', 'Precio actual de BTC')

if __name__ == '__main__':
    # Iniciamos un servidor interno en el puerto 8000
    start_http_server(8000)
    print("Nexus Exporter ejecutándose en el puerto 8000...")
    
    while True:
        # Aquí llamarías a tu lógica de Aircrack-ng o API de Binance
        NETWORK_TRAFFIC.set(random.uniform(0, 100)) 
        CRYPTO_PRICE.set(65000 + random.uniform(-100, 100))
        
        time.sleep(5)
