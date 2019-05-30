# -*- coding: utf-8 -*-
import time
from datetime import datetime

from page.page_main import MainPage


def test_study_case01(init_test):
    main = MainPage()
    p_study = main.switch_study()
    p_study.swipe_up(600, 3)
    for article in p_study.get_article_list():
        # start_time = datetime.now()
        # print(p_study.is_article(article))
        # stop_time = datetime.now()
        # print(stop_time - start_time)
        p_article = p_study.tap_article(article)
        time.sleep(3)
        print(p_article.verify_page_visible())
        p_article.go_back()
        p_study.open_group()
        time.sleep(3)
