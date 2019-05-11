# Raspberrypi-mqtt-message
First step for my project making a locker functions with an application.    

```mermaid
graph LR
A[Hard edge] -->B(Round edge)
```

I used Cloudmqtt for posting messages.     
Sends message pressed every time I press the switch connected to my Raspberry pi
### Circuit Structure
![Alt text](GPIO_Switch/Circuit_GPIO_Swtich.png)

![Alt text](GPIO_Switch/CloudMQTT_switch_pressed.png)
`import paho.mqtt.client as mqtt`

