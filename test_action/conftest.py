# -*- coding: utf-8 -*-
import pytest

from driver.base_driver import BaseDriver
from setting import Setting as ST


@pytest.fixture(scope='function')
def init_test():
    BaseDriver.init_driver(port=ST.PORT, udid=ST.UDID)
    yield init_test
    BaseDriver.quit_driver()
