import ibmiotf.application
import ibmiotf.device
import time
import random
import sys
from twilio.rest import Client 
account_sid = 'AC18b4d7a136b9a07a181a837c23ad1358'
auth_token ='adc9782f6520041c84ac4930daad0625 '
client = Client(account_sid, auth_token) 

organization = "wbp1fk"
deviceType = "ESP32"
deviceId = "sensor_data_1"
authMethod = "token"
authToken = "prototype_1"

pH = random.randint(1, 14)
turbidity = random.randint(1, 1000)
temperature = random.randint(0, 100)
info=""

def myCommandCallback(cmd):
    print("Command Received: %s" % cmd.data['command'])
    print(cmd)


try:
    deviceOptions={"org":organization,"type":deviceType,
                   "id":deviceId,"auth-method":authMethod,"auth-token":authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)

except Exception as e:
    print("caught exception connecting device: %s" % str(e))
    sys.exit()

deviceCli.connect()

while True:

    pH = random.randint(1, 14)
    turbidity = random.randint(1, 1000)
    temperature = random.randint(0, 100)

    if temperature>70 or pH<6 or pH>8 or turbidity>500:
        print("high")
        info="harmfull to drink"
        message = client.messages.create(from_='+14632588702',
                                         body ='This water is harmfull to drink',
                                         to ='+91 95856 XXXXX')
    else:
        info="capable to drinking"
        message = client.messages.create(from_='+14632588702',
                                         body ='This water is good to drink',
                                         to ='+91 95856 XXXXX')
    data = {'pH': pH, 'turbid': turbidity,'temp': temperature,'info':info}


    def myOnPublishCallback():
        print("Published pH= %s" % pH, "Turbidity:%s" % turbidity,
              "Temperature:%s" % temperature)

    success = deviceCli.publishEvent("demo", "json", data, qos=0, on_publish=myOnPublishCallback)
    if not success:
        print("Not Connected to ibmiot")
    time.sleep(5)
    deviceCli.commandCallback = myCommandCallback

deviceCli.disconnect()
