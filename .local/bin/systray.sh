#/bin/sh

if pgrep stalonetray > /dev/null; then
  killall stalonetray
else
  stalonetray --config ~/.config/stalonetray/config.conf & 
fi
