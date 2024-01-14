from Funciones import check_port_status, send_telegram_message
import asyncio
import os

# Configuración que realizo para la prueba
url = "https://httpstat.us/503"
telegram_token = os.environ.get("TELEGRAM_TOKEN")
telegram_chat_id = os.environ.get("TELEGRAM_CHAT_ID")

estado_web = check_port_status(url)

mensaje = f"Prueba dinámica realizada. Estado de la web {url}: {estado_web}"
asyncio.run(send_telegram_message(telegram_token, telegram_chat_id, mensaje))
