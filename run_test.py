# -*- coding: utf-8 -*-
from multiprocessing import Process

import pytest

from service.server import Server
from setting import Setting
from utils.ope_run_data import OpeRunData


def run_test_action(index):
    Setting.UDID = OpeRunData().get_value(f'device_{index}', 'udid')
    Setting.PORT = OpeRunData().get_value(f'device_{index}', 'port')
    pytest.main(['--alluredir=.report', 'test_action/test_get_score.py'])


if __name__ == '__main__':
    s = Server()
    s.start_appium_server()

    for i in range(len(s.device_list)):
        p = Process(target=run_test_action, args=(i,))
        p.start()
        p.join()
