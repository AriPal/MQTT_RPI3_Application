import time
import datetime
import Adafruit_DHT
import paho.mqtt.client as mqtt
from system_info import get_temperature
import psutil 
mqttc = mqtt.Client()
mqttc.connect("iot.eclipse.org", 1883, 60)
mqttc.loop_start()


while True:
    try:
	cpu_usage = psutil.cpu_percent()
	tmp = get_temperature()  
        if cpu_usage is None or tmp is None:
            time.sleep(2)
            continue 
        now = datetime.datetime.now()
        dt = now.replace(microsecond=0)
        print(dt)
        print('Temperature: {0:0.1f} C'.format(tmp))
        print('Cpu usage:    {0:0.1f} %'.format(cpu_usage))
        mqttc.publish("aripal", "%s" % dt)
        mqttc.publish("aripal", "Temperature: %.1f C" % tmp)
        mqttc.publish("aripal", "CPU Usage:    %.1f Percent" % cpu_usage)
        time.sleep(2)
    except KeyboardInterrupt:
        exit()
