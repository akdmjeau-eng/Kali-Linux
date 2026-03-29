import os
from prometheus_client import Gauge, Counter

# Métrica para contar cuántos handshakes hemos capturado
HANDSHAKES_DETECTED = Counter('nexus_wpa_handshakes_total', 'Total de handshakes capturados')
DEAUTH_ALERTS = Gauge('nexus_deauth_active', 'Alerta de ataque de desautenticación activo')

def check_for_handshake():
    # Buscamos archivos .cap o logs de airodump
    if os.path.exists("nexus_scan-01.kismet.csv"):
        with open("nexus_scan-01.kismet.csv", "r") as f:
            content = f.read()
            if "WPA handshake" in content:
                HANDSHAKES_DETECTED.inc()
                print("¡ALERTA: Handshake capturado!")
