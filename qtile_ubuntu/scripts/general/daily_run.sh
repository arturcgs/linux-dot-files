#!/bin/sh

# backup logseq
echo fazendo backup do logseq...
cp -ru /home/artur/HDD/Documents/logseq /home/artur/HDD/GDrive/pessoal
echo backup finalizado

# update e upgrade
sudo apt update -y && sudo apt upgrade -y