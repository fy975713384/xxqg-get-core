# -*- coding: utf-8 -*-
from service.command import Command as Cmd


class Port:

    @classmethod
    def create_port_list(cls, start_port: int, device_list: list) -> list:
        port_list = []
        if not device_list:
            raise RuntimeError('设备未连接，生成可用端口失败！')
        while len(port_list) < len(device_list):
            if not cls._is_port_used(start_port):
                port_list.append(start_port)
            start_port += 1
        return port_list

    @classmethod
    def _is_port_used(cls, port):
        return Cmd.is_port_used(port)
