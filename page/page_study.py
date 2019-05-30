# -*- coding: utf-8 -*-
import random

from appium.webdriver import WebElement

from page.base_page import BasePage
from page.page_article import ArticlePage


class StudyPage(BasePage):
    def __init__(self):
        self._article_list = (self.MB.XPATH, '//android.widget.ListView/android.widget.FrameLayout')
        self._group_button = (self.MB.XPATH, '//*[@resource-id="view_pager"]/android.widget.FrameLayout')

    def get_article_list(self) -> list:
        return self.find_all(self._article_list)[1:-1]

    def get_article_by_num(self, num) -> WebElement:
        return self.get_article_list()[num]

    @classmethod
    def tap_article(cls, article: WebElement):
        article.click()
        return ArticlePage()

    @classmethod
    def get_video_time(cls, article: WebElement):
        _list = article.find_elements_by_xpath('//*[contains(@text, ":")]')
        if _list:
            return _list[0].get_attribute('text')
        else:
            return None

    def open_group(self):
        self.find(self._group_button).click()

    @classmethod
    def switch_section(cls, section: str):
        pass

    @classmethod
    def is_article(cls, article: WebElement):
        # 文章需要有日期
        _date = article.find_elements_by_xpath('//*[starts-with(@text,"2019-")]')
        if len(_date) == 0: return False
        # 文章不应该有播放时间
        _time = article.find_elements_by_xpath('//*[contains(@text, ":")]')
        if len(_time) != 0: return False
        # # 文章不应该有播放进度条
        # _seek = article.find_elements_by_class_name('android.widget.SeekBar')
        # if len(_seek) != 0: return False
        # 文章不包含专题两个字
        _special = article.find_elements_by_xpath('//*[contains(@text, "专题")]')
        if len(_special) != 0: return False
        # TODO: 需要提升判断效率
        return True

    @classmethod
    def simulate_page_turning(cls):
        _num = random.randint(2, 5)
        for _ in range(_num):
            cls.swipe_up()


'''
new UiScrollable(new UiSelector().resourceId("cn.xuexi.android:id/view_pager")).setAsHorizontalList().scrollIntoView(new UiSelector().text("订阅"))
new UiScrollable(new UiSelector().className("android.widget.ListView")).setAsHorizontalList().scrollIntoView(new UiSelector().text("订阅"))
'''
