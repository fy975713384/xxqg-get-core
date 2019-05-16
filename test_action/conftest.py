# -*- coding: utf-8 -*-
import pytest

from dirver.base_driver import BaseDriver


@pytest.fixture(scope='function')
def init_test():
    BaseDriver.init_driver()
    yield init_test
    BaseDriver.get_driver().quit()
