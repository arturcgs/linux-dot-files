#!/bin/sh

# backup logseq
echo fazendo backup do logseq...
cp -ru /home/artur/HDD/Documents/logseq /home/artur/HDD/GDrive/pessoal
echo backup finalizado

# update do neovim
curl https://github.com/neovim/neovim/releases/download/nightly/nvim.appimage \
      -Lo ~/.local/bin/nvim --create-dirs
chmod u+x ~/.local/bin/nvim

# update e upgrade
sudo nala update
sudo nala upgrade