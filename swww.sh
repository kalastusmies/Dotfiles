#!/bin/bash

DIR=$HOME/Wallpapers/
PICS=($(ls ${DIR}))

RANDOMPICS=${PICS[ $RANDOM % ${#PICS[@]} ]}

if [[ $(pidof swaybg) ]]; then
  pkill swaybg
fi

swww query || swww-daemon

#change-wallpaper using swww
wal -i ${DIR}/${RANDOMPICS};swww img ${DIR}/${RANDOMPICS} --transition-fps 30 --transition-type any --transition-duration 3; notify-send -e -u low "Wallpaper changed." -i ${DIR}/${RANDOMPICS}; pywalfox update;
