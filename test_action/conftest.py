# -*- coding: utf-8 -*-
import allure
import pytest

from driver.base_driver import BaseDriver
from setting import Setting as ST


@pytest.fixture(scope='function')
def init_test():
    BaseDriver.init_driver(port=ST.PORT, udid=ST.UDID)
    yield init_test
    BaseDriver.quit_driver()


@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    _driver = BaseDriver.get_driver()
    outcome = yield
    resp = outcome.get_result()
    if resp.when == 'call' and resp.failed:
        f = _driver.get_screenshot_as_png()
        allure.attach(f, '错误截图', allure.attachment_type.PNG)
        logcat = _driver.get_log('logcat')
        c = '\n'.join([i['message'] for i in logcat])
        allure.attach(c, '错误日志', allure.attachment_type.TEXT)
        # if _driver.get_app_pid() != _driver.apppid:
        #     raise Exception('设备进程 ID 变化，可能发生崩溃')
