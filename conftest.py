# content of conftest.py
import pytest
from datetime import datetime
import os
import logging

# 动态生成日志文件名,每次运行生成独立日志文件
def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    config.option.log_file = os.path.join("logs", f"bd_pytest.{timestamp}")  

# 执行开始执行，写入日志
@pytest.fixture(autouse=True)
def fun_log(request):
    module_name = request.module.__name__
    test_name = request.node.name  # 获取调用此 fixture 的测试函数名称
    logging.info("当前运行的测试函数：{}".format(module_name+'.'+test_name))


# 案例失败，写入错误日志
def pytest_exception_interact(node, call, report):
    # 当测试用例抛出异常时触发
    if report.failed:
        logger = logging.getLogger(__name__)
        error_message = call.excinfo.getrepr(style="short")
        logger.error(f"case failed : {node.name}\nerror_message :\n{error_message}")