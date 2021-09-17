# SAS (Simple alarm service)<br/>_Wakes you up with your favourite music_

## Instructions
1. Clone this repository under $HOME/.local/bin
```
mkdir -p ~/.local/bin ~/.config ~/.config/systemd/user && git clone https://github.com/bonohub13/simple_alarm_service ~/.config/alarm
```
2. Add ~/.local/bin to $PATH
```
echo "$PATH" | grep "$HOME/.local/bin" || echo "export PATH=$HOME/.local/bin" >> ~/.profile
```
3. Run the ```init_setup.sh``` under alarm
```
cd ~/.config/alarm && ./init_setup.sh
```
4. To enable and start the service, run the following command.
```
systemctl --user enable --now alarm.service
```
