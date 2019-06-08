# -*- coding: utf-8 -*-
from page.page_main import MainPage


def test_av_case01(init_test):
    main = MainPage()
    # 验证点击视听按钮显示视听页面
    p_av = main.switch_av()
    assert p_av.verify_page_visible()
    # 验证可以切换到其它频道
    l1 = p_av.get_article_list()
    p_av.switch_channel('短视频')
    l2 = p_av.get_article_list()
    assert l1[0] != l2[0]
