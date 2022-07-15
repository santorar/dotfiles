#!/bin/bash
[ "$XDG_SESSION_TYPE" = x11 ] || exit 0
nvidia-settings --assign CurrentMetaMode="nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On } "
sleep 1
xrandr --current --output DVI-I-0 --gamma 0.98:0.98:0.94 
xrandr --current --output VGA-1-1 --gamma 0.85:0.85:0.85

