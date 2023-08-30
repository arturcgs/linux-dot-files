#!/bin/sh

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

# set 2nd screen resolution
run xrandr --output eDP-1 --primary --mode 1366x768 --pos 0x0 --rotate normal --output HDMI-1 --mode 1920x1080 --pos 1366x0 --rotate normal --output DP-1 --off

# set wallpaper
run feh --bg-scale /home/artur/Pictures/wallpaper/soviet_space.png

# autolock
#xautolock -time 15 -locker "systemctl suspend" -detectsleep &

# google drive mount
#run rclone mount gdrive: /home/arturcgs/HDD/GDrive --daemon

# run picom
run picom -b --experimental-backends --config ~/.config/qtile/picom.conf

# run mate-polkit, to be able to save sudo on codium
#run /usr/lib/mate-polkit/polkit-mate-authentication-agent-1

# run applets
run flameshot
run nm-applet