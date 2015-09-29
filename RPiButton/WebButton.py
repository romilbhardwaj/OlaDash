import RPi.GPIO as GPIO
import time
import urllib2

#Setup your OlaDash server here:
OlaDash_url = "http://127.0.0.1:8080/requestcab"
GPIO_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    current_input = GPIO.input(GPIO_PIN)
    if current_input == False:
        print('Push button pressed!')
        urllib2.urlopen(OlaDash_url).read()        
        time.sleep(0.2)