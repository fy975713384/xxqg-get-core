# -*- coding: utf-8 -*-
from utils.command import Command


class Server:
    @classmethod
    def init_server(cls):
        cmd = Command()
        cmd.exec_command(cmd.START_APPIUM)
