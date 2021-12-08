# Rain Alert

## Sobre
Notificador via SMS alertando se vai chover na localidade.

## Como funciona
Utilizando os dados da API do [OpenWeather](https://openweathermap.org/), é informado, via SMS através do [Twilio](https://www.twilio.com) se a principal condição atmosférica da região para as próximas 12 horas terá o [código 700 ou inferior](https://openweathermap.org/weather-conditions), o que indica que vai chover. Se confirmado, então enviará uma SMS para que carregue guarda-chuva.

## O que pode ser melhorado
- Implementar o script na nuvem.
- Criar um bot no Telegram ou WhatsApp, em vez do Twilio.

