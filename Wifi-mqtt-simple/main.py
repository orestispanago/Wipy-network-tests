from mqtt import MQTTClient
from network import WLAN
import machine
import time
from credentials import ssid, password, broker_ip, mqtt_user, mqtt_pass, topic

def sub_cb(topic, msg):
   print(msg)

wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid, auth=(WLAN.WPA2, password), timeout=5000)

while not wlan.isconnected():
    machine.idle()
print("Connected to WiFi\n")
print("IP:", wlan.ifconfig()[0])

client = MQTTClient("device_id", broker_ip,user=mqtt_user, password=mqtt_pass, port=1883)

client.set_callback(sub_cb)
client.connect()
# client.subscribe(topic=topic)

while True:
    print("Sending ON")
    client.publish(topic=topic, msg="ON")
    time.sleep(5)
    print("Sending OFF")
    client.publish(topic=topic, msg="OFF")
    # client.check_msg()

    time.sleep(5)
