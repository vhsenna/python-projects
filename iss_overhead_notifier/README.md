# ISS Overhead Notifier

## Sobre
Notificador por e-mail de quando a Estação Espacial Internacional (ISS) sobrevoar as coordenadas imputadas e que seja visível, ou seja, durante a noite.

## Como funciona
Através da biblioteca `requests` são feitas requisições a duas APIs.

A primeira, [International Space Station Current Location](http://open-notify.org/Open-Notify-API/ISS-Location-Now/), para receber as coordenadas da ISS em tempo real.

A segunda, [Sunset and sunrise times API](https://sunrise-sunset.org/api), para receber os horários do pôr e do nascer do sol para uma determinada latitude e longitude.

Cruzando estas duas informações, a biblioteca `smtplib` enviará um e-mail notificando.

