# -*- coding: utf-8 -*-
import os
import platform

from utils.logger import logger


class Command:
    START_APPIUM = 'appium'
    ADB_DEVICES = 'adb devices'

    if platform.system().lower() == 'windows':
        CHECK_PORT = 'netstat -ano | findstr '
        LIST_RUNNING_SERVER = "tasklist | findstr 'node.exe'"
        KILL_APPIUM_PROCESS = "taskkill -F -PID 'node.exe'"

        @classmethod
        def kill_appium_server(cls):
            cls._exec_command(cls.KILL_APPIUM_PROCESS)

    elif platform.system().lower() == 'darwin':
        CHECK_PORT = 'lsof -i:'
        LIST_RUNNING_SERVER_PID = "ps -ef | grep 'node' | awk '/[A|a]ppium/{print $2}'"
        KILL_PROCESS_BY_PID = "kill -9"

        @classmethod
        def kill_appium_server(cls):
            server_pid_list = cls._get_command_result(cls.LIST_RUNNING_SERVER_PID)
            for pid in server_pid_list:
                cls._exec_command(f'{cls.KILL_PROCESS_BY_PID} {pid}')

    # TODO: Windows 下需要考虑下直接杀掉 node.exe 进程会不会影响其它程序的运行
    # TODO: 需要考虑下其它系统的兼容性

    @classmethod
    def get_device_list(cls):
        device_list = []
        res = cls._get_command_result(cls.ADB_DEVICES)
        if len(res) <= 1:
            raise RuntimeError('设备未连接！')
        for r in res:
            if 'List' in r:
                continue
            device_info = r.split('\t')
            if device_info[1].lower() == 'device':
                device_list.append(device_info[0])
        logger.info(f'当前设备列表：{device_list}')
        return device_list

    @classmethod
    def is_port_used(cls, port) -> bool:
        res = cls._get_command_result(f'{cls.CHECK_PORT}{str(port)}')
        return True if len(res) > 0 else False

    @classmethod
    def start_appium(cls, port, bp, device):
        command = f'{cls.START_APPIUM} -p {port} -bp {bp} -U {device} --session-override --no-reset'
        logger.info(command)
        cls._exec_command(command)

    @classmethod
    def _exec_command(cls, command: str):
        return os.system(command)

    @classmethod
    def _get_command_result(cls, command: str) -> list:
        result_list = []
        result = os.popen(command).readlines()
        if len(result) > 0:
            for r in result:
                if r == '\n':
                    continue
                result_list.append(r.strip('\n'))
        return result_list
