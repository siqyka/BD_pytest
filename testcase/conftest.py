# content of conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os
import logging

    
@pytest.fixture()
def browser():
    """
    # 创建浏览器驱动的fixture
    # 用于打开和关闭浏览器
    """
    # 配置Chrome选项
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')  # 最大化窗口
    # 初始化浏览器驱动
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def baidu_page(browser):
    """
    # 打开百度首页的fixture
    # 依赖browser fixture
    """
    # 打开百度首页
    browser.get("https://www.baidu.com")
    # 返回浏览器对象
    return browser


# 模块共用的fixture
# @pytest.fixture(scope='module', autouse=True)
# def baidu_page(browser):
#     """
#     # 打开百度首页的fixture
#     # 依赖browser fixture
#     """
#     # 打开百度首页
#     browser.get("https://www.baidu.com")
#     # 返回浏览器对象
#     return browser