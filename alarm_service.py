#!/usr/bin/python
import configparser
from random import randint
from datetime import datetime
from time import sleep
from os import system, path
import sys

class ReadConfig:
    def __init__(self):
        config_file = f"homedir/.config/alarm.conf"
        # DEFAULT and COMMON is in config
        self.config = configparser.ConfigParser(
                interpolation=configparser.ExtendedInterpolation(),
                delimiters=":",
                inline_comment_prefixes="#"
        )
        self.config.read(config_file)

    def get_default(self) -> dict:
        return self.config["DEFAULT"]

    def get_paths(self) -> dict:
        return self.config["Paths"]

class Alarm:
    def __init__(self):
        self.config = ReadConfig()
        self.update_values()

    def update_values(self):
        self.msg = self.config.get_default()["Message"]
        self.songs = self.config.get_default()["Songs"].split("\n")
        self.target_day = self.config.get_default()["DayOfWeek"].split("\n")
        self.target_time = ":".join(self.config.get_default()["Time"].split("\n"))
        self.retval = 0
        self.now = datetime.now().strftime("%H:%M:%S")
        self.today = datetime.today().strftime("%A")
        self.song = self.songs[randint(0, len(self.songs))] if len(self.songs) > 1 else self.songs[0]

    def run(self):
        try:
            while True:
                self.update_values()

                if self.today in self.target_day \
                        and self.now == self.target_time:
                    self.retval = system(f"{self.config.get_paths()['src_dir']}/alarm.sh '{self.song}' '{self.msg}'")
                if self.retval != 0:
                    break

                sleep(1.0)
        except KeyboardInterrupt:
            sys.exit(-1)

        sys.exit(self.retval)

if __name__ == "__main__":
    alarm = Alarm()
    alarm.run()
