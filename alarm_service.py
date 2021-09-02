#!/usr/bin/python
import configparser
from random import randint
from datetime import datetime
from os import system, path

class ReadConfig:
    def __init__(self):
        config_file = f"{path.dirname(path.abspath(__file__))}/alarm.conf"
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
        self.msg = self.config.get_default()["Message"]
        self.songs = self.config.get_default()["Songs"].split("\n")
        self.target_day = self.config.get_default()["DayOfWeek"].split("\n")
        self.target_time = ":".join(self.config.get_default()["Time"].split("\n"))

    def run(self):
        now = datetime.now().strftime("%H:%M:%S")
        today = datetime.today().strftime("%A")
        song = self.songs[randint(0, len(self.songs))] if len(self.songs) > 1 else self.songs[0]

        if today in self.target_day and now == self.target_time:
            system(f"{self.config.get_paths()['src_dir']}/alarm.sh '{song}' '{self.msg}'")

if __name__ == "__main__":
    alarm = Alarm()
    alarm.run()
