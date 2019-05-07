##Test code for checking if mqtt connection is going well  
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.username_pw_set("knolxopk","ACzTwH7__yCY")
client.connect("m24.cloudmqtt.com",12712)
client.publish("topic/iopi","test")
