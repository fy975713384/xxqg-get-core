# -*- coding: utf-8 -*-
import time
from datetime import datetime

import allure

from page.page_main import MainPage


@allure.step
def test_study_case01(init_test):
    main = MainPage()
    # 验证点击学习按钮显示学习页面
    p_study = main.switch_study()
    assert p_study.verify_page_visible()
    # 验证可以切换到其它频道
    l1 = p_study.get_article_list()
    p_study.switch_channel('要闻')
    l2 = p_study.get_article_list()
    assert l1[0] != l2[0]
