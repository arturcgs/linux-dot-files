#!/usr/bin/env bash

# Store the STDOUT of fzf in a variable
selection=$(find /home/artur/code /home/artur/Documents /home/artur/Downloads /home/artur/HDD/Documents /home/artur/HDD/Temporario /home/artur/Pictures /home/artur/Programs /home/artur/Scripts \( ! -regex '.*/\..*' \) -type d | fzf --multi --height=80% --border=sharp \
--preview='tree -C {}' --preview-window='45%,border-sharp' \
--prompt='Dirs > ' \
--bind='del:execute(rm -ri {+})' \
--bind='ctrl-p:toggle-preview' \
--bind='ctrl-d:change-prompt(Dirs > )' \
--bind='ctrl-d:+reload(find /home/artur/code /home/artur/Documents /home/artur/Downloads /home/artur/HDD/Documents /home/artur/HDD/Temporario /home/artur/Pictures /home/artur/Programs /home/artur/Scripts -type d)' \
--bind='ctrl-d:+change-preview(tree -C {})' \
--bind='ctrl-d:+refresh-preview' \
--bind='ctrl-f:change-prompt(Files > )' \
--bind='ctrl-f:+reload(find /home/artur/code /home/artur/Documents /home/artur/Downloads /home/artur/HDD/Documents /home/artur/HDD/Temporario /home/artur/Pictures /home/artur/Programs /home/artur/Scripts -type f)' \
--bind='ctrl-f:+change-preview(cat {})' \
--bind='ctrl-f:+refresh-preview' \
--bind='ctrl-a:select-all' \
--bind='ctrl-x:deselect-all' \
--header '
CTRL-D to display directories | CTRL-F to display files
CTRL-A to select all | CTRL-x to deselect all
ENTER to edit | DEL to delete
CTRL-P to toggle preview
'
)

# Determine what to do depending on the selection
if [ -d "$selection" ]; then
    cd "$selection" || exit
elif [ -f "$selection" ]; then
    eval "$EDITOR $selection"
fi