# -*- coding: utf-8 -*-
import allure
import pytest

from page.page_article import ArticlePage
from page.page_main import MainPage
from page.page_score import ScorePage


@pytest.mark.parametrize('opt', ['read', 'view'])
def test_get_rv_score(init_test, opt):
    open_score_page()
    score = get_score_by_option(opt)
    if score < 6:
        p_opt = goto_opt_page_from_score_page(opt)
        while score < 6:
            art_list = get_cur_art_list(p_opt)
            for article in art_list:
                if is_article(p_opt, article):
                    simulate_read(p_opt, article, score)
                    score += 1
                    if score == 6:
                        return
            simulate_tp_after_loop(p_opt)


@allure.step('打开得分页面')
def open_score_page():
    p_main = MainPage()
    p_main.switch_user().switch_score()


@allure.step('获取 <{opt}> 的得分')
def get_score_by_option(opt) -> int:
    p_score = ScorePage()
    return p_score.get_my_score(opt)


@allure.step('进入 <{opt}> 页面')
def goto_opt_page_from_score_page(opt):
    p_score = ScorePage()
    if opt == 'read':
        p_read = p_score.go_to_read()
        p_read.switch_channel('要闻')
        return p_read
    elif opt == 'view':
        p_view = p_score.go_to_av()
        return p_view
    else:
        raise RuntimeError(f'选项错误：不存在 <{opt}> 选项')


@allure.step('获取 {p_opt} 页面文章列表')
def get_cur_art_list(p_opt) -> list:
    return p_opt.get_article_list()


@allure.step('判断 {p_opt} 中的 {art} 是否符合条件')
def is_article(p_opt, art) -> bool:
    return p_opt.is_article(art)


@allure.step('模拟阅读')
def simulate_read(p_opt, article, score):
    _time = p_opt.get_video_time(article)
    p_art = p_opt.tap_article(article)
    p_art.simulate_read(p_opt.sign, _time)
    share_art(p_opt.sign, score)
    p_opt.go_back()


@allure.step('分享文章，如果 "{opt}"=="read" && "{score}"为偶数')
def share_art(opt, score):
    if opt == 'read' and score % 2 == 0:
        p_share = ArticlePage().share_to_xxqg()
        p_share.choose_my_group()
        p_share.send_share_content()


@allure.step('当结束一轮循环后翻页')
def simulate_tp_after_loop(p_opt):
    p_opt.simulate_page_turning()
