import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,sys,os
import logging


def test_clickmore(baidu_page):
    # 定位更多按钮元素
    more_element = baidu_page.find_element(By.CSS_SELECTOR, "#s-top-left > div > a")
    # 创建 ActionChains 对象
    actions = webdriver.ActionChains(baidu_page)
    # 将鼠标移动到更多按钮上
    actions.move_to_element(more_element).perform()
    time.sleep(1)  # 等待悬停效果显示
    ti=baidu_page.find_element(By.CSS_SELECTOR, "#s-top-more > div:nth-child(1) > a")
    # 点击悬浮窗中的翻译链接
    assert ti.text=="翻译"
    logging.info("step more pass")
    baidu_page.find_element(By.CSS_SELECTOR, "#s-top-more > div:nth-child(1)").click()
    handles = baidu_page.window_handles
    # 切换到最新打开的窗口
    baidu_page.switch_to.window(handles[-1])
    # 等待页面加载完成
    WebDriverWait(baidu_page, 10).until(EC.title_contains("百度翻译"))
    # 获取网页标题
    title = baidu_page.title
    assert title == "百度翻译_领先的AI大模型翻译_支持文本/文档/图片翻译"
    logging.info("step fanyi pass")
    logging.info("case test_clickmore pass")