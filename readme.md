## radio bluetooth set up
1. im terminal bluetoothctl eingeben, enter
2. eingeben (nach jedem befehl enter): power on, scan on, agent on
3. warten bis geraet gefunden wird, mac adresse (xx:xx:xx:xx:xx:xx) aufschreiben
4. eingeben (mit enter): pair macadresse, trust macadresse, connect macadresse
5. mit quit und enter wird bluetoothctl verlassen, wieder im normalen terminal
6. im terminal nano ~/.asoundrc eingeben, oeffnet textdatei mit 4 zeilen
7. bestehende macadresse ersetzen (anfuehrungszeichen behalten!)
8. mit strg+x nano verlassen, mit y und enter bestaetigen
9. im terminal pacmd set-card-profile bluez_card.xx_xx_xx_xx a2dp sink eingeben (unterstrich in macadresse)
10. im terminal pacmd set-default-sink bluez_sink.xx_xx_xx_xx.a2dp_sink eingeben
11. sudo reboot, sollte jetzt funktionieren

## autostart set up
1. in terminal: nano /home/pi/.bashrc
2. in letzter zeile pfad zum skirpt angeben, momentan radio, .bashrc spielt programm, wenn neues terminal geoeffnet wird
3. mit strg+x nano verlassen, mit y und enter bestaetigen
4. raspberry muss beim start terminal oeffnen, darum nano ~/.config/lxsession/LXDE-pi/autostart im terminal eingeben
5. in letzter zeile steht @lxterminal, oeffnet terminal beim start
6. strg+x um nano verlassen, y und enter bestaetigen
7. sudo reboot im terminal, sollte funktionieren. 

