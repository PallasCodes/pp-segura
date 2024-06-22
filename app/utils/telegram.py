import requests
import sys
import os

# Agregar esta información por usuario como parte de su registro
TOKEN = '7051302207:AAFD7o0oXbqhBjYE-RZq0OeCCG7zMoR--R4'
# CHAT_ID = '7379503467'

URL = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s'


def send_message(chat_id, message):
    """
    Envía el mensaje establecido al bot configurado en las
    variables constantes.

    mensaje: str
    returns: bool, True si se pudo mandar el mensaje, False de lo contrario
    """
    try:
        respuesta = requests.get(URL % (TOKEN, chat_id, message))       
        
        if not respuesta.status_code == 200:
            return False
        return True
    except:
        return False
    
