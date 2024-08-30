import paho.mqtt.publish as publish

publish.single("ifn649", "LED_ON", hostname="54.252.147.242")
print("Done")