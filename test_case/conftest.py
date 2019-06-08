# -*- coding: utf-8 -*-
import pytest

from driver.base_driver import BaseDriver


@pytest.fixture(scope='function')
def init_test():
    BaseDriver.init_driver()
    yield init_test
    BaseDriver.quit_driver()
