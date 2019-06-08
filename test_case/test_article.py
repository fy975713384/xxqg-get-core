# -*- coding: utf-8 -*-
import time

from page.page_main import MainPage


def test_article_case01(init_test):
    p_main = MainPage()
    p_study = p_main.switch_study()
    time.sleep(2)
    p_study.switch_channel('要闻')
    time.sleep(2)
    al = p_study.get_article_list()
    p_art = p_study.tap_article(al[0])
    p_art.tap_share()
    p_art.tap_xxqg_on_popup()
