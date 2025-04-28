import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,sys,os
import logging


class Test_Navigation_Bar():
    @pytest.mark.smoke
    def test_homepage(self,baidu_page):
        # 获取网页标题
        title = baidu_page.title
        # assert title == "百度一下，你就知道1"
        assert title == "百度一下，你就知道"
        logging.info("case test_homepage pass")

    @pytest.mark.smoke  
    def test_clicknews(self,baidu_page):
        # 点击新闻链接
        baidu_page.find_element(By.LINK_TEXT, "新闻").click()#s-top-left > a:nth-child(1)
        # 获取所有窗口句柄
        handles = baidu_page.window_handles
        # 切换到最新打开的窗口
        baidu_page.switch_to.window(handles[-1])
        # 等待页面加载完成
        WebDriverWait(baidu_page, 10).until(EC.title_contains("百度新闻"))
        # 获取网页标题
        title = baidu_page.title
        assert title == "百度新闻——海量中文资讯平台"
        logging.info("case test_clicknews pass")

    @pytest.mark.smoke  
    def test_clickhao123(self,baidu_page):
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

    @pytest.mark.smoke   
    def test_clickmap(self,baidu_page):
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
        logging.info("case test_clickmap pass")
        
    def test_clickmore(self,baidu_page):
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
        
    