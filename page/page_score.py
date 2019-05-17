# -*- coding: utf-8 -*-
from page.base_page import BasePage
import re

from page.page_video import VideoPage
from page.page_study import StudyPage


class ScorePage(BasePage):
    def __init__(self):
        self._title = (self.MB.ID, 'title')
        self._read = (self.MB.ACCESSIBILITY_ID, '阅读文章')
        self._read_score = (self.MB.XPATH, '//*[@content-desc="阅读文章"]/../*[starts-with(@content-desc,"已获")]')
        self._read_study = (self.MB.XPATH, '//*[@content-desc="阅读文章"]/../*[@content-desc="去看看"]')
        self._audio = (self.MB.ACCESSIBILITY_ID, '视听学习')
        self._audio_score = (self.MB.XPATH, '//*[@content-desc="视听学习"]/../*[starts-with(@content-desc,"已获")]')
        self._audio_study = (self.MB.XPATH, '//*[@content-desc="视听学习"]/../*[@content-desc="去看看"]')

    def get_my_score(self, opt) -> int:
        _options = {"read": self._read_score,
                    "view": self._audio_score
                    }
        _content = self.find(_options[opt]).get_attribute('content-desc')
        _score = re.search(r'\d', _content).group()
        _score = int(_score)
        return _score

    def go_to_read(self):
        self.find(self._read_study).click()
        return StudyPage()

    def go_to_view(self):
        self.find(self._audio_study).click()
        return VideoPage()
