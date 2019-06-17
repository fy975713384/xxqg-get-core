# -*- coding: utf-8 -*-

from page.page_read import StudyPage


class AVPage(StudyPage):
    def __init__(self):
        super(AVPage, self).__init__()
        self.sign = 'view'
        self._channel_first = (self.MB.XPATH, '//*[@text="第一频道"]')

    def verify_page_visible(self):
        return self.find(self._channel_first).is_displayed()

    @classmethod
    def is_article(cls, article):
        # 视频文章需要有日期
        cls.set_implicitly_wait(0.2)
        _date = article.find_elements_by_xpath('//*[starts-with(@text,"2019-")]')
        _flag = True if len(_date) > 0 else False
        cls.set_implicitly_wait(6)
        return _flag
