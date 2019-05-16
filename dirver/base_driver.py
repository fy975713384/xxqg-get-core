# -*- coding: utf-8 -*-

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from utils.logger import logger


class BaseDriver:

    _driver = None

    @classmethod
    def get_driver(cls) -> WebDriver:
        return cls._driver

    @classmethod
    def init_driver(cls):
        logger.info('初始化 Android driver...')
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Phone",
            "automationName": "UiAutomator2",
            "appPackage": "cn.xuexi.android",
            "appActivity": "com.alibaba.android.rimet.biz.SplashActivity",
            "appWaitActivity": "com.alibaba.android.rimet.biz.home.activity.HomeActivity",
            "autoGrantPermissions": True,
            "noReset": True
        }
        cls._driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        cls._driver.implicitly_wait(6)
        logger.info('driver 初始化完成！')
        return cls._driver
