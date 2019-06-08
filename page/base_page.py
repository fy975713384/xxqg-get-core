# -*- coding: utf-8 -*-
from xml import etree

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from driver.base_driver import BaseDriver
from utils.logger import logger


class BasePage:
    MB = MobileBy

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BasePage, cls).__new__(cls)
        return cls.instance

    @classmethod
    def _find_by(cls, by=MB.ID, value=None) -> WebElement:
        try:
            return BaseDriver.get_driver().find_element(by=by, value=value)
        except NoSuchElementException:
            logger.critical(f'元素未找到!\nby -> {by}\nexpression -> {value}')

    @classmethod
    def find(cls, locator) -> WebElement:
        return cls._find_by(*locator)

    @classmethod
    def find_all(cls, locator) -> list:
        return BaseDriver.get_driver().find_elements(*locator)

    @classmethod
    def find_by_xml(cls, xpath):
        page_source = BaseDriver.get_driver().page_source
        xml = etree.XML(str(page_source).encode('utf-8'))
        return xml.xpath(xpath)

    @classmethod
    def go_back(cls):
        BaseDriver.get_driver().back()

    @classmethod
    def get_size(cls) -> tuple:
        """
        获取当前屏幕尺寸
        """
        size = BaseDriver.get_driver().get_window_size()
        return size['width'], size['height']

    @classmethod
    def swipe(cls, dire: str, duration=None, num: int = 1):
        """
        封装原生 swipe 方法，指定滑动方向和位置
        :param dire: only `up` `down` `left` `right`
        :param duration: (optional) time to take the swipe, in ms.
        :param num: should bigger than 1
        :return:
        """
        x = cls.get_size()[0] / 2
        y = cls.get_size()[1] / 2
        if dire == 'up' or dire == 'down':
            y0 = cls.get_size()[1] / 10 * 6
            y1 = cls.get_size()[1] / 10 * 4
            if dire == 'down':
                y0, y1 = y1, y0
            for _ in range(num):
                BaseDriver.get_driver().swipe(x, y0, x, y1, duration)

        elif dire == 'left' or dire == 'right':
            x0 = cls.get_size()[0] / 4 * 3
            x1 = cls.get_size()[0] / 4 * 1
            if dire == 'right':
                x0, x1 = x1, x0
            for _ in range(num):
                BaseDriver.get_driver().swipe(x0, y, x1, y, duration)
        else:
            logger.error('滑动方向错误')

    @classmethod
    def swipe_down(cls, duration=None, num: int = 1):
        """
        模拟手指向下滑动
        """
        cls.swipe('down', duration, num)

    @classmethod
    def swipe_up(cls, duration=None, num: int = 1):
        """
        模拟手指向上滑动
        """
        cls.swipe('up', duration, num)

    @classmethod
    def swipe_right(cls, duration=None, num: int = 1):
        """
        模拟手指向右滑动
        """
        cls.swipe('right', duration, num)

    @classmethod
    def swipe_left(cls, duration=None, num: int = 1):
        """
        模拟手指向左滑动
        """
        cls.swipe('left', duration, num)

    @classmethod
    def get_toast(cls):
        _toast = (cls.MB.CLASS_NAME, 'android.widget.Toast')
        cls.find(_toast).get_attribute('text')

    @classmethod
    def set_implicitly_wait(cls, time_to_wait):
        BaseDriver.get_driver().implicitly_wait(time_to_wait)

    # @staticmethod
    # def set_implicitly_wait(time_to_wait):
    #     def decorator(func):
    #         def wrapper(*args, **kwargs):
    #             BasePage.change_implicitly_wait(time_to_wait)
    #             return func(*args, **kwargs)
    #
    #         BasePage.change_implicitly_wait(6)
    #         return wrapper
    #
    #     return decorator
