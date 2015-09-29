# OlaDash - Get your Ola at the push of a button!  

A quick hack to get an Ola cab at your location at the press of your Amazon Dash. Since I do not have an Amazon Dash to play with (yet), I've written a quick script to make your friendly Raspberry Pi with a push button connected to the GPIO act as a replacement for the Amazon dash.  

## Setup

* OlaDashServer - Setup your location coordinates in /OlaDashServer/settings.py and run "python manage.py makemigrations" followed by "python manage.py runserver 0.0.0.0:8000". *insert Ola auth process here once you get the API keys*

* RPiButton - Configure the server address in WebButton.py and make it run at startup by adding this line to your /etc/rc.local in your RPi - "(sleep 5;python *Address to WebButton.py*)&"

## Current Status

Waiting for the Ola Cabs API authorization. Might also write a python wrapper for the Ola API.