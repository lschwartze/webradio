## radio bluetooth set up
1. in terminal enter bluetoothctlr
2. enter the following in new lines respectively power on, scan on, agent on
3. wait until device was found, note down mac adress (xx:xx:xx:xx:xx:xx)
4. then enter: pair macadresse, trust macadresse, connect macadresse
5. using "quit" and enter leave bluetoothctl
6. enter nano ~/.asoundrc eingeben, opens text file with 4 rows
7. enter mac adress including quotation marks
8. leave nano with ctrl+x
9. in terminal pacmd set-card-profile bluez_card.xx_xx_xx_xx a2dp sink using underscores in mac adress
10. in terminal pacmd set-default-sink bluez_sink.xx_xx_xx_xx.a2dp_sink
11. sudo reboot

## autostart set up
1. in terminal: nano /home/pi/.bashrc
2. in last row enter path to script, called "radio", .bashrc runs code when new terminal is opened
3. leave nano with ctrl+x
4. raspberry needs to open terminal on start, thus nano ~/.config/lxsession/LXDE-pi/autostart in terminal
5. last row says @lxterminal, opens terminal on startup
6. strg+x
7. sudo reboot

