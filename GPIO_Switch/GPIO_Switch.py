import RPi.GPIO as GPIO 
import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.username_pw_set("knolxopk","ACzTwH7__yCY")
client.connect("m24.cloudmqtt.com",12712)

##subscribe clients (cloudmqtt)

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(14, GPIO.IN) # Set GPIO pin 14 as input

def rising_edge_callback(channel):
	print('UP on Channel', channel)
	client.publish("Switch","Pressed") # Publish "Pressed" when switch is pressed
	
GPIO.add_event_detect(14, GPIO.RISING,
	callback=rising_edge_callback, bouncetime=300)

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	print('Exit.....')
finally:
	GPIO.cleanup()