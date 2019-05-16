# -*- coding: utf-8 -*-
from page.base_page import BasePage
from page.page_score import ScorePage


class UserPage(BasePage):

    def __init__(self):
        self._app_title = (self.MB.ACCESSIBILITY_ID, '我的应用')
        self._score = (self.MB.ACCESSIBILITY_ID, '学习积分')

    def get_title(self):
        self.find(self._app_title).text()

    def switch_score(self):
        self.find(self._score).click()
        return ScorePage()
