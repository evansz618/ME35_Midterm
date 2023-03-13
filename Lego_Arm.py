import machine
import Paths

import LED
from secrets import Tufts_eecs as wifi
import mqtt_CBR

# Sets IP Address and Topic
mqtt_broker = '10.247.55.202' 
topic_sub = 'minecraft'
topic_pub = 'minecraft'
client_id = 'EvanArduino'

# Initializes connection to broker
def _init_():
    mqtt_CBR.connect_wifi(wifi)
    fred = mqtt_CBR.mqtt_client(client_id, mqtt_broker, whenCalled)
    fred.subscribe(topic_sub)
    return fred

# Sends angle to broker
def send_angle(shoulder_angle, knee_angle, fred):
    shoulder_angle = str(shoulder_angle)
    knee_angle = str(knee_angle)
    message = "("+shoulder_angle+","+knee_angle+")"
    fred.publish(topic_pub, message)
    
# Main code that runs to send angles to broker and light up LED lights 
def main():
    fred = _init_()
    for i in range(len(Paths.shoulder)):
        shoulder = Paths.shoulder[i]
        knee = Paths.knee[i]
        send_angle(shoulder,knee,fred)
        LED.wave_on()
        LED.wave_off()