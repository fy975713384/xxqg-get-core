# -*- coding: utf-8 -*-
import pytest

from page.page_main import MainPage


@pytest.mark.flaky
@pytest.mark.parametrize(
    "option", ['read', 'view']
)
def test_get_rv_score(init_test, option):
    main = MainPage()
    p_score = main.switch_user().switch_score()
    score = int(p_score.get_my_score(option))
    if score < 16:
        p_study = p_score.go_to_read() if option == 'read' else p_score.go_to_view()
        while score < 16:
            p_study.simulate_page_turning()
            article_list = p_study.get_article_list()
            if len(article_list) > 0:
                for article in article_list:
                    if p_study.is_article(article):
                        time_ = p_study.get_video_time(article)
                        p_article = p_study.tap_article(article)
                        p_article.simulate_read(option, time_)
                        p_study.go_back()
                        score += 1
                        if score == 6: break
