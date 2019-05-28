# -*- coding: utf-8 -*-
import os


class Command:
    START_APPIUM = 'appium'
    LIST_ADB_DEVICES = 'adb devices'

    @classmethod
    def exec_command(cls, command):
        return os.system(command)
