#!/bin/bash

# get current time 
current_time=`date +"%H:%M"`
final_time=`date -d '+25 minutes' '+%H:%M'`

# Messages
echo "Iniciando Pomodoro de 25 minutos"
echo "Início: $current_time"
echo "Final : $final_time"
sleep 5m
echo "Faltam 20 minutos"

sleep 5m
echo "Faltam 15 minutos"

sleep 5m
echo "Faltam 10 minutos"

sleep 5m
echo "Faltam 5 minutos"

sleep 5m

# Send a notification
echo "Final da Sessão de Trabalho!"
notify-send "Aviso" "Final da Sessão de trabalho!"

# Play a sound
paplay /home/artur/Documents/sounds/alarm-clock.wav

# Sleep for 6 minutes
sleep  6m

# Send a notification
echo "Final da pausa!"
notify-send "Aviso" "Final da pausa!"

# Play a sound
paplay /home/artur/Documents/sounds/alarm-clock.wav
