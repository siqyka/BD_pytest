import pytest
import sys
import os
import logging


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        # 获取当前文件路径
        mainfile_path = os.path.dirname(os.path.abspath(__file__))   
        # 使用os.path.join方法安全地连接路径
        current_path=os.path.join(mainfile_path,'testcase')
        path = os.path.join(current_path, filename)
        logging.info("Run Testcase Path:"+path)
        pytest.main(["-vs",path])
    except:
        logging.info("No Testcase Filename")
        logging.info("Run ALL Testcase")
        # print("No Testcase Filename")
        # print("Run ALL Testcase")
        pytest.main(["-vs","./testcase"])
