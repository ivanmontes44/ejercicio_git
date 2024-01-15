# tests/test_funciones.py
import asyncio
from unittest.mock import patch
import pytest
from Funciones import check_port_status, send_telegram_message, monitor_website

def test_check_port_status():
    assert check_port_status("https://httpstat.us/200") == "OK"
    

@pytest.mark.asyncio
async def test_send_telegram_message():
    await send_telegram_message("dummy_token", "dummy_chat_id", "Mensaje de prueba")
    

@patch('Funciones.check_port_status')
def test_monitor_website(mock_check):
    mock_check.return_value = "OK"
    
    # Teniendo en cuenta que monitor_website es una función asíncrona y 
    # que se ha modificado para aceptar un parámetro adicional 'test_mode'
    # que realiza una sola iteración para fines de prueba
    async def run_test():
        status = await monitor_website("https://httpstat.us/200", 0, "dummy_token", "dummy_chat_id", test_mode=True)
        assert status == "OK"

    asyncio.run(run_test())
