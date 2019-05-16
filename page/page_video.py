# -*- coding: utf-8 -*-
from page.page_study import StudyPage


class VideoPage(StudyPage):
    def __init__(self):
        super(VideoPage, self).__init__()

    @classmethod
    def is_article(cls, article):
        # 视屏文章需要有日期
        _date = article.find_elements_by_xpath('//*[starts-with(@text,"2019-")]')
        _flag = True if len(_date) > 0 else False
        return _flag
