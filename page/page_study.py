# -*- coding: utf-8 -*-
import random

from appium.webdriver import WebElement

from page.base_page import BasePage
from page.page_article import ArticlePage


class StudyPage(BasePage):
    def __init__(self):
        self._article_list = (self.MB.XPATH, '//android.widget.ListView/android.widget.FrameLayout')

    def get_article_list(self) -> list:
        return self.find_all(self._article_list)

    def get_article_by_num(self, num) -> WebElement:
        return self.get_article_list()[num]

    @classmethod
    def tap_article(cls, article: WebElement):
        article.click()
        return ArticlePage()

    @classmethod
    def is_article(cls, article: WebElement):
        # 文章需要有日期
        _date = article.find_elements_by_xpath('//*[starts-with(@text,"2019-")]')
        _flag = True if len(_date) > 0 else False
        # 文章不应该有播放进度条
        _seek = article.find_elements_by_class_name('android.widget.SeekBar')
        _flag = True if len(_seek) == 0 else False
        return _flag

    @classmethod
    def simulate_page_turning(cls):
        _num = random.randint(7, 11)
        for _ in range(_num):
            cls.swipe_up()


'''
new UiScrollable(new UiSelector().resourceId("cn.xuexi.android:id/view_pager")).setAsHorizontalList().scrollIntoView(new UiSelector().text("订阅"))
new UiScrollable(new UiSelector().className("android.widget.ListView")).setAsHorizontalList().scrollIntoView(new UiSelector().text("订阅"))
'''
