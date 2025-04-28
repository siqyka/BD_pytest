import logging
def fun_log(func):
    def wrapper(*args,**kwargs):
        logging.info("test222222")
        return func(*args,**kwargs)