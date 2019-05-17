# -*- coding: utf-8 -*-
import random
import time
from page.base_page import BasePage
from page.page_choose_linkman import LinkManPage
from utils.logger import logger


class ArticlePage(BasePage):
    def __init__(self):
        self._share = (self.MB.ID, 'my_news_avatar')
        self._share_xxqg = (self.MB.XPATH, '//*[contains(@text, "学习强国")]/..')

    def tap_share(self):
        self.find(self._share).click()

    def share_to_xxqg(self):
        self.tap_share()
        self.find(self._share_xxqg).click()
        return LinkManPage()

    @classmethod
    def simulate_read(cls, opt='read', time_: str = None):
        if opt == 'read':
            _num = random.randint(23, 29)
            for _ in range(_num):
                cls.swipe_up(_num * 47)
                time.sleep(_num % 20)
        if opt == 'view':
            _sec = int(time_.split(':')[0]) * 60 + int(time_.split(':')[1])
            for _ in range(_sec // 47):
                # 防止 Appium 等待 60s 强行停止
                time.sleep(47)
                cls.swipe_up()
            time.sleep(_sec % 47)
        else:
            logger.critical('模拟阅读模式选项错误！')
