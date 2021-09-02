#!/usr/bin/sh

echo "Configuring alarm.conf for you..."
sed -i "s/username/$HOME/" alarm.conf

echo "Configuring alarm.service for you..."
sed -i -e "s.homedir.$HOME." -e "s.username.$USER." alarm.service
sleep 1

echo "Configuring alarm.service"
mkdir -p ~/.config/systemd
cp alarm.service ~/.config/systemd/
echo 'Done!'

echo "Enable the service with systemctl --user enable --now alarm.service"
