#!/bin/sh

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

# set 2nd screen resolution
run xrandr --output eDP-1-1 --primary --mode 1366x768 --pos 0x0 --rotate normal --output HDMI-1-1 --mode 1920x1080 --pos 1366x0 --rotate normal --output DP-1-1 --off

# set wallpaper
run feh --bg-scale /home/arturcgs/HDD/Pictures/wallpaper/soviet_space.png

# autolock
run xautolock -time 15 -locker "/home/arturcgs/Scripts/qtile/sleep.sh" -detectsleep

# run picom
run picom -b --experimental-backends --config ~/.config/qtile/picom.conf

# run mate-polkit, to be able to save sudo on codium
run /usr/lib/mate-polkit/polkit-mate-authentication-agent-1

# run applets
run flameshot
run nm-applet