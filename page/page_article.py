# -*- coding: utf-8 -*-
import random

from page.base_page import BasePage


class ArticlePage(BasePage):
    def __init__(self):
        self._share = (self.MB.ID, 'my_news_avatar')

    @classmethod
    def simulate_read(cls, opt='read'):
        if opt == 'read':
            _num = random.randint(23, 37)
            for _ in range(_num):
                cls.swipe_up()
        if opt == 'view':
            # appium 60秒不操作则自动停止
            for _ in range(2):
                _sec = random.randint(30, 50)
                import time
                time.sleep(_sec)
                cls.swipe_up()
