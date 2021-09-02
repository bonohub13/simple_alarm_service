#!/usr/bin/sh

alarm() {
    file="songs.conf"
    song=$1
    pacat --file-format="$(file "$song" | awk -F: '{print $2}' | awk '{print $1}' | tr "[:upper:]" "[:lower:]")" "$song" & \
        notify-send "$2"

    return 0
}

ALARM_RUNNING=0
ps aux | grep "pacat" | while read line; do
    [ "$#" -gt 0 ] && echo "$line" | awk '{for (i=11;i < NF;i++) {printf "%s", $i} print ""}' | grep "pacat --file-format=flac $1" && ALARM_RUNNING=1
done

if [ "$#" -eq 1 ] && [ "$ALARM_RUNNING" -eq 0 ];then
    alarm "$1" 'WAKE UP! Time for work!'
    sleep 1
    return 0
elif [ "$#" -eq 2 ] && [ "$ALARM_RUNNING" -eq 0 ]; then
    alarm "$1" "$2"
    sleep 1
    return 0
else ([ "$#" -eq 0 ] || [ "$#" -gt 2 ]) && [ "$ALARM_RUNNING" -eq 0 ]
    echo "Error: Invalid number of arguments"
    return 1
fi
