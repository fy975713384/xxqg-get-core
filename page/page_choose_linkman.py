# -*- coding: utf-8 -*-
from page.base_page import BasePage
import time


class LinkManPage(BasePage):
    def __init__(self):
        self._my_study_group = (self.MB.ID, 'session_item')
        self._popup_send_button = (self.MB.XPATH, '//*[@text="发送"]')

    def choose_my_group(self):
        self.find(self._my_study_group).click()

    def send_share_content(self):
        self.find(self._popup_send_button).click()
        time.sleep(2)
        # TODO: 寻找方法替代掉 sleep
