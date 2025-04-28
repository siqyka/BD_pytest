import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,sys,os
import logging
    
@pytest.mark.smoke    
def test_homepage1(baidu_page):
    # 获取网页标题
    title = baidu_page.title
    # assert title == "百度一下，你就知道1"
    assert title == "百度一下，你就知道"
    logging.info("case test_homepage pass")

def test_clickhao1231(baidu_page):
    # 点击hao123链接，通过CSS选择器定位元素
    baidu_page.find_element(By.CSS_SELECTOR, "#s-top-left > a:nth-child(2)").click()
    # 获取所有窗口句柄
    handles = baidu_page.window_handles
    # 切换到最新打开的窗口
    baidu_page.switch_to.window(handles[-1])
    # 等待页面加载完成
    WebDriverWait(baidu_page, 10).until(EC.title_contains("hao123"))
    # 获取网页标题
    title = baidu_page.title
    assert title == "hao123_上网从这里开始"
    logging.info("case test_hao123 pass")


def test_clickmap1(baidu_page):
    handles = baidu_page.window_handles
    # 切换到最新打开的窗口
    baidu_page.switch_to.window(handles[-1])
    # 关闭最新打开的窗口
    baidu_page.close()
    # 切换回主窗口
    baidu_page.switch_to.window(handles[0])
    # 点击地图链接，通过XPATH选择器定位元素
    baidu_page.find_element(By.XPATH, '//*[@id="s-top-left"]/a[3]').click()
    # 获取所有窗口句柄
    handles = baidu_page.window_handles
    # 切换到最新打开的窗口
    baidu_page.switch_to.window(handles[-1])
    # 等待页面加载完成
    WebDriverWait(baidu_page, 10).until(EC.title_contains("百度地图"))
    # 获取网页标题
    title = baidu_page.title
    assert title == "百度地图"
    logging.info("case map pass")