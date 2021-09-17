#!/usr/bin/sh -eux

echo "Configuring alarm.conf for you..."
sed -i "s/username/$USER/" alarm.conf

echo "Configuring alarm.service for you..."
echo "$PATH" | grep "$HOME/.local/bin" || PATH="$PATH:$HOME/.local/bin"
sed -i -e "s,path$,$PATH," alarm.service
sed -i -e "s.homedir.$HOME." -e "s.username.$USER." alarm.service
sleep 1

echo "Configuring alarm.service"
mkdir -p ~/.config/systemd
cp alarm.service ~/.config/systemd/user
sleep 1
echo 'Done!'

echo "Configuring alarm_service.py"
mkdir -p ~/.local/bin
sed -i -e "s.homedir.$HOME." alarm_service.py
cp alarm_service.py ~/.local/bin
sleep 1
echo 'Done!'

echo "Enable the service with systemctl --user enable --now alarm.service"
