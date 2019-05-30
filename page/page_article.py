# -*- coding: utf-8 -*-
import random
import time
from page.base_page import BasePage
from utils.logger import logger


class ArticlePage(BasePage):
    def __init__(self):
        self._share = (self.MB.ID, 'my_news_avatar')
        self._share_xxqg = (self.MB.XPATH, '//*[contains(@text, "学习强国")]/..')
        self._base_webview = (self.MB.ID, 'common_webview')

    def tap_share(self):
        self.find(self._share).click()

    def share_to_xxqg(self):
        self.tap_share()
        self.find(self._share_xxqg).click()
        from page.page_choose_linkman import LinkManPage
        return LinkManPage()

    def verify_page_visible(self) -> bool:
        return self.find(self._base_webview).is_displayed()

    @classmethod
    def simulate_read(cls, opt='read', time_: str = None):
        if opt == 'read':
            logger.info(f'开始模拟阅读...')
            _num = random.randint(13, 19)
            for _ in range(_num):
                cls.swipe_up(_num * 47)
                time.sleep(_num % 10)
        elif opt == 'view' and time_ is not None:
            _sec = int(time_.split(':')[0]) * 60 + int(time_.split(':')[1])
            logger.info(f'开始播放视频：{_sec}s')
            for _ in range(_sec // 47):
                # 防止 Appium 等待 60s 强行停止
                time.sleep(47)
                cls.swipe_up()
        else:
            logger.critical(f'模拟阅读错误！\n阅读模式：<{opt}>\n模拟时间：<{time_}>')
