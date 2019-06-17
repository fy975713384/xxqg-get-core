# -*- coding: utf-8 -*-
import time
from page.base_page import BasePage
from page.page_choose_linkman import LinkManPage
from utils.logger import logger


class ArticlePage(BasePage):
    def __init__(self):
        self._share_button = (self.MB.XPATH,
                              '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView[2]')
        self._share_xxqg = (self.MB.XPATH, '//*[contains(@text, "学习强国")]/..')
        self._share_page = (self.MB.ID, 'pager')
        self._base_webview = (self.MB.ID, 'common_webview')

    def tap_share(self):
        self.find(self._share_button).click()
        if not self.find(self._share_page).is_displayed():
            logger.critical('分享操作出现异常')
            raise RuntimeError()

    def tap_xxqg_on_popup(self):
        self.find(self._share_xxqg).click()
        return LinkManPage()

    def share_to_xxqg(self):
        self.tap_share()
        return self.tap_xxqg_on_popup()

    def verify_page_visible(self) -> bool:
        return self.find(self._base_webview).is_displayed()

    @classmethod
    def simulate_read(cls, opt, time_: str = None):
        if opt == 'read':
            if time_ is not None:
                logger.error(f'阅读时间错误，time 应该为 None，但它现在是 <{time_}>')
            logger.info(f'开始模拟阅读...')
            for i in range(4):
                time.sleep(30)
                cls.swipe_up()

        if opt == 'view':
            _sec = int(time_.split(':')[0]) * 60 + int(time_.split(':')[1])
            logger.info(f'获取播放时间：{time_}  开始播放视频：{_sec}s')
            for _ in range(_sec // 47):
                # 防止 Appium 等待 60s 强行停止
                time.sleep(40)
                cls.swipe_up()
