# -*- coding: utf-8 -*-
from threading import Thread

from service.command import Command as Cmd
from service.port import Port
from utils.ope_run_data import OpeRunData


class Server:

    def __init__(self):
        self.device_list = self._get_device_list()
        self.appium_port_list = self._create_port_list(start_port=4700)
        self.bootstrap_port_list = self._create_port_list(start_port=4900)
        self.run_data = OpeRunData()

    @classmethod
    def _get_device_list(cls) -> list:
        return Cmd.get_device_list()

    def _create_port_list(self, start_port):
        return Port.create_port_list(start_port, self.device_list)

    def _start_appium_server_ordinal(self, index):
        port = str(self.appium_port_list[index])
        bp = str(self.bootstrap_port_list[index])
        device = self.device_list[index]
        self.run_data.write_data(index, port, bp, device)
        Cmd.start_appium(port, bp, device)

    def stop_appium_server(self):
        self.run_data.clear_yaml()
        Cmd.kill_appium_server()

    def start_appium_server(self):
        self.stop_appium_server()

        for i in range(len(self.device_list)):
            appium_start = Thread(target=self._start_appium_server_ordinal, args=(i,))
            appium_start.start()

        import time
        time.sleep(7)
