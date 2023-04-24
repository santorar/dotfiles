#!/bin/bash
song=$(playerctl --player=spotify metadata title 2> /dev/null)
artist=$(playerctl --player=spotify metadata artist 2> /dev/null)
status=$(playerctl --player=spotify status 2> /dev/null)
error="No players found"
paused="Paused"

if [ "$song" = "" ] || [ "$status" = "$paused" ]; then
  echo ""
else
  current="$song - $artist"
  echo "$current"
fi
