#!/bin/bash
[ "$XDG_SESSION_TYPE" = x11 ] || exit 0
nvidia-settings --assign CurrentMetaMode="nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On } "
sleep 1
xrandr --current --output DVI-I-0 --gamma 0.8:0.8:0.8 --brightness 1
xrandr --current --output VGA-1-1 --gamma 0.65:0.65:0.65 --brightness 1

