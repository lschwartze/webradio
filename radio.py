#***BLUETOOTH SETUP***
#Mac-adress used to pair, trust, connect within bluetoothctl terminal
#set mac-adress in ~/.asoundrc
#pacmd set-card-profile bluez_card.xx_xx_xx_xx a2dp sink
#pacmd set-default-sink bluez_sink.xx_xx_xx_xx.a2dp_sink

#***AUTOSTART SETUP***
#edited ~/.config/lxsession/LXDE-pi/autostart
#@lxterminal -e python3 /home/pi/radio.py runs this script on boot.

import webbrowser
import urllib.request
from tkinter import *
import os
import subprocess

#button commands
def antenne_vorarlberg():
    os.system("pkill chromium")
    webbrowser.open('https://radios.co.at/antenne-vorarlberg/')
    
def bayern_drei():
    os.system("pkill chromium")
    webbrowser.open('https://www.internetradio-horen.de/bayern-3')
    
def kronehit():
    os.system("pkill chromium")
    webbrowser.open('https://radios.co.at/kronehit/')
    
def radio_vorarlberg():
    os.system("pkill chromium")
    webbrowser.open('https://radios.co.at/radio-vorarlberg/')
    
def drs_drei():
    os.system("pkill chromium")
    webbrowser.open('https://www.srf.ch/play/radio/livepopup/radio-srf-3')

def youtube():
    os.system("pkill chromium")
    webbrowser.open('https://www.youtube.com/')
    
def rock_antenne():
    os.system("pkill chromium")
    webbrowser.open('https://www.rockantenne.de/webradio/live')

#start radio in default channel
def start():
    webbrowser.open('https://www.internetradio-horen.de/bayern-3')
    
def shutdown():
    os.system("sudo shutdown -h now")
    
#check internet connection
status = 'checking'
while status == 'checking':
    try:
        urllib.request.urlopen('https://www.google.com')
        status = 'connected'
    except:
        status = 'checking'
    
#start 2nd process that attempts to connect to bluetooth
subprocess.Popen(["python", 'BT.py'])
        
start()

#gui
radio = Tk()
radio.title("Internetradio, brought to you by Laurin Schwartze Corporation")
radio.attributes('-zoomed', True)

antenne_vorarlberg_button = Button(radio, text= "Antenne Vorarlberg", command = antenne_vorarlberg, height = 3, width = 20)

bayern_drei_button = Button(radio, text = "Bayern 3", command = bayern_drei, height = 3, width = 20)

kronehit_button = Button(radio, text = "Kronehit", command = kronehit, height = 3, width = 20)

radio_vorarlberg_button = Button(radio, text= "Radio Vorarlberg", command = radio_vorarlberg, height = 3, width = 20)

drs_drei_button = Button(radio, text = "DRS3", command = drs_drei, height = 3, width = 20)

youtube_button = Button(radio, text = "Youtube", command = youtube, height = 3, width = 20)

rock_antenne_button = Button(radio, text = "Rock Antenne", command = rock_antenne, height = 3, width = 20)

shutdown_button = Button(radio, text = "power off", command = shutdown, height = 3, width = 20, bg = "red")

#make it look sorta ok
antenne_vorarlberg_button.grid(row=0, column=0, pady=10)
bayern_drei_button.grid(row=1, column=0, pady=10)
kronehit_button.grid(row=2, column=0, pady=10)
radio_vorarlberg_button.grid(row=3, column=0, pady=10)
drs_drei_button.grid(row=4, column=0, pady=10)
youtube_button.grid(row=0, column=2, pady=10, padx=5)
rock_antenne_button.grid(row=1, column=2, pady=10, padx=5)
shutdown_button.grid(row=2, column=2, pady=10, padx=5)

radio.mainloop()