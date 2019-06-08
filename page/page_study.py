# -*- coding: utf-8 -*-
import random

from appium.webdriver import WebElement
from selenium.common.exceptions import NoSuchElementException

from page.base_page import BasePage
from page.page_article import ArticlePage
from page.page_channel import ChannelPage
from utils.logger import logger


class StudyPage(BasePage):
    def __init__(self):
        self.sign = 'read'
        self._channel_recommend = (self.MB.XPATH, '//*[@text="推荐"]')
        self._channel_button = (self.MB.XPATH, '//*[@text="推荐"]/../../following-sibling::android.widget.FrameLayout')
        self._article_list = (self.MB.XPATH, '//android.widget.ListView/android.widget.FrameLayout')

    def verify_page_visible(self):
        return self.find(self._channel_recommend).is_displayed()

    def get_article_list(self) -> list:
        return self.find_all(self._article_list)[1:-1]

    def get_article_by_num(self, num) -> WebElement:
        return self.get_article_list()[num]

    def open_channel_group(self):
        self.find(self._channel_button).click()
        return ChannelPage()

    @classmethod
    def tap_article(cls, article: WebElement):
        article.click()
        return ArticlePage()

    @classmethod
    def get_video_time(cls, article: WebElement):
        cls.set_implicitly_wait(1)
        _list = article.find_elements_by_xpath('//*[contains(@text, ":")]')
        cls.set_implicitly_wait(6)
        if _list:
            return _list[0].get_attribute('text')
        else:
            return None

    @classmethod
    def is_article(cls, article: WebElement):
        cls.set_implicitly_wait(0.2)
        # 文章需要有日期
        _date = article.find_elements_by_xpath('//*[starts-with(@text,"2019-")]')
        if len(_date) == 0:
            cls.set_implicitly_wait(6)
            return False
        # 文章不应该有播放时间
        _time = article.find_elements_by_xpath('//*[contains(@text, ":")]')
        if len(_time) != 0:
            cls.set_implicitly_wait(6)
            return False
        # # 文章不应该有播放进度条
        # _seek = article.find_elements_by_class_name('android.widget.SeekBar')
        # if len(_seek) != 0: return False
        # 文章不包含专题两个字
        _special = article.find_elements_by_xpath('//*[contains(@text, "专题")]')
        if len(_special) != 0:
            cls.set_implicitly_wait(6)
            return False
        # TODO: 需要更优雅地实现设置隐式等待时间
        cls.set_implicitly_wait(6)
        return True

    @classmethod
    def switch_channel(cls, channel: str):
        _channel = (cls.MB.XPATH, f'//*[@text="{channel}"]/..')
        try:
            cls.find(_channel).click()
        except NoSuchElementException:
            logger.critical(f'该频道不存在，请检查：{channel}')

    @classmethod
    def simulate_page_turning(cls):
        _num = random.randint(2, 5)
        for _ in range(_num):
            cls.swipe_up()


'''
new UiScrollable(new UiSelector().resourceId("cn.xuexi.android:id/view_pager")).setAsHorizontalList().scrollIntoView(new UiSelector().text("订阅"))
new UiScrollable(new UiSelector().className("android.widget.ListView")).setAsHorizontalList().scrollIntoView(new UiSelector().text("订阅"))
'''
