import os
from libreria_bot_telegram_monitor_web import monitor_website, check_port_status, send_telegram_message

#  Configuración
url = "https://httpstat.us/503"  # URL a monitorear
interval =   60 # Intervalo en segundos
telegram_token = os.environ.get("TELEGRAM_TOKEN")
telegram_chat_id = os.environ.get("TELEGRAM_CHAT_ID")


# Iniciamos el monitor
monitor_website(url, interval, telegram_token, telegram_chat_id)


