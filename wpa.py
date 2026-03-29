import requests

def send_nexus_alert(message):
    token = "TU_API_TOKEN_AQUI"
    chat_id = "TU_CHAT_ID_AQUI"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": f"⚠️ [NEXUS SYSTEM v3.0] ⚠️\n{message}"}
    
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Error enviando alerta: {e}")

# Ejemplo de uso cuando detectas el handshake:
# send_nexus_alert("¡Handshake capturado en la red: Casa_Wifi!")
