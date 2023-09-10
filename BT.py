#this script tries to connect to speaker continuously
#if that does not work something went very wrong
from time import sleep
import os
while True:
    os.system("bluetoothctl -- connect 7C:96:D2:94:D1:AF")
    sleep(10)