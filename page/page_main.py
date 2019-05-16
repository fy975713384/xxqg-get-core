# -*- coding: utf-8 -*-

from page.base_page import BasePage
from page.page_study import StudyPage
from page.page_user import UserPage


class MainPage(BasePage):

    def __init__(self):
        self._message = (self.MB.ID, 'home_bottom_tab_button_message')
        self._ding = (self.MB.ID, 'home_bottom_tab_button_ding')
        self._article = (self.MB.ID, 'home_bottom_tab_button_work')
        self._audio = (self.MB.ID, 'home_bottom_tab_button_contact')
        self._user = (self.MB.ID, 'home_bottom_tab_button_mine')

    def switch_message(self):
        self.find(self._message).click()
        return

    def switch_ding(self):
        self.find(self._ding).click()
        return

    def switch_article(self):
        self.find(self._article).click()
        return StudyPage()

    def switch_audio(self):
        self.find(self._audio).click()

    def switch_user(self):
        self.find(self._user).click()
        return UserPage()
