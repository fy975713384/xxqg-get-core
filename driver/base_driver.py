# -*- coding: utf-8 -*-

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from utils.logger import logger


class BaseDriver:
    _driver: WebDriver = None

    @classmethod
    def get_driver(cls) -> WebDriver:
        return cls._driver

    @classmethod
    def quit_driver(cls):
        logger.info('测试完成，退出 driver！')
        cls._driver.quit()

    @classmethod
    def init_driver(cls, port, udid: str = None) -> WebDriver:
        logger.info('初始化 Android driver...')
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Phone",
            "udid": f"{udid}",
            "automationName": "UiAutomator2",
            "appPackage": "cn.xuexi.android",
            "appActivity": "com.alibaba.android.rimet.biz.SplashActivity",
            "appWaitActivity": "com.alibaba.android.rimet.biz.home.activity.HomeActivity",
            "autoGrantPermissions": True,
            "noReset": True
        }
        cls._driver = webdriver.Remote(f"http://localhost:{port}/wd/hub", desired_caps)
        cls._driver.implicitly_wait(13)
        logger.info('driver 初始化完成！')
        return cls._driver
