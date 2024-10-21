# rain-alert
A Python script that sends an SMS alert via Twilio when rain is forecasted within the next 4 hours using OpenWeatherMap's weather API.


English Description
Weather Alert with Twilio SMS Integration

This Python script fetches weather data from the OpenWeatherMap API for a specific location and sends an SMS alert using Twilio if rain is forecasted within the next few hours. The message alerts the user to bring an umbrella when rain is expected.

Features:
Weather Forecasting: Uses the OpenWeatherMap API to retrieve a 4-hour forecast for a specific location (configured by latitude and longitude).
Twilio SMS Alert: Integrates with Twilio to send an SMS alert if rain is forecasted.
Automated Check: Loops through the weather conditions and checks for precipitation codes to determine if rain is likely.
Customizable Location: The latitude and longitude can be easily changed to monitor the weather in different regions.

Technologies:
	Python: Main language for the script.
	Requests: For fetching weather data from the OpenWeatherMap API.
	Twilio API: To send SMS messages based on weather conditions.

_________________________________________________________________________________________________________________________________________________________________________________



Descripción en Castellano
Alerta Meteorológica con Integración de SMS de Twilio

Este script en Python obtiene datos meteorológicos de la API de OpenWeatherMap para una ubicación específica y envía una alerta por SMS usando Twilio si se pronostican lluvias en las próximas horas. El mensaje alerta al usuario para llevar un paraguas cuando se espera lluvia.

Funcionalidades:
Pronóstico del Tiempo: Utiliza la API de OpenWeatherMap para obtener un pronóstico de 4 horas para una ubicación específica (configurada por latitud y longitud).
Alerta SMS de Twilio: Se integra con Twilio para enviar una alerta por SMS si se pronostican lluvias.
Chequeo Automatizado: Recorre las condiciones meteorológicas y verifica los códigos de precipitación para determinar si es probable que llueva.
Ubicación Personalizable: La latitud y longitud se pueden cambiar fácilmente para monitorear el clima en diferentes regiones.

Tecnologías:
	Python: Lenguaje principal del script.
	Requests: Para obtener datos meteorológicos de la API OpenWeatherMap.
	API de Twilio: Para enviar mensajes SMS basados en las condiciones meteorológicas.
