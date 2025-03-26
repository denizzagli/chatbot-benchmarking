from selenium import webdriver
from utils.logger import get_logger
from utils import config

logger = get_logger()

def get_web_driver():
    logger.info("Cretaion of web driver for Chrome is starting.")
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(config.WINDOW_SIZE)
    driver = webdriver.Chrome(options=options)

    logger.info("Cretaion of web driver was ended.")
    
    return driver