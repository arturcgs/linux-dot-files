#!/bin/bash

# Sleep for 25 minutes
sleep 25m

# Send a notification to both screens
notify-send "Aviso" "Final da Sessão de trabalho!"

# Play a sound (adjust the path to your sound file)
paplay /home/artur/Documents/sounds/alarm-clock.wav

# Sleep for 6 minutes
sleep  6m

# Send a notification to both screens
notify-send "Aviso" "Final da pausa!"

# Play a sound (adjust the path to your sound file)
paplay /home/artur/Documents/sounds/alarm-clock.wav
