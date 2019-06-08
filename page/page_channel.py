# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException

from page.base_page import BasePage
from utils.logger import logger


class ChannelPage(BasePage):
    def __init__(self):
        self._root_xpath = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout'
        self._title = (self.MB.XPATH, f'{self._root_xpath}//*[text="全部频道"]')
        self._close_button = (self.MB.XPATH, f'{self._root_xpath}//*[@text="全部频道"]/following-sibling::android.widget.ImageView')

    def select_channel(self, channel: str):
        _channel = (self.MB.XPATH, f'{self._root_xpath}//*[@text="{channel}"]/../..')
        try:
            self.find(_channel).click()
        except NoSuchElementException:
            logger.critical(f'该频道不存在，请检查：{channel}')
