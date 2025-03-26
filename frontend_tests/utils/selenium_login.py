import time
from utils import config
from utils.logger import get_logger

from selenium.webdriver.common.by import By

logger = get_logger()

def login(driver):
    logger.info("Login operation is starting. Username: " + config.CHATBOT_USERNAME + ". Password: " + config.CHATBOT_PASSWORD + ".")
    
    email_input = driver.find_element(By.XPATH, "//input[@id='email']")
    email_input.send_keys(config.CHATBOT_USERNAME)

    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.send_keys(config.CHATBOT_PASSWORD)

    login_button = driver.find_element(By.XPATH, "//button[@type='button' and contains(@class, 'ant-btn-primary')]")
    login_button.click()

    time.sleep(2)
    
    logger.info("Login operation was ended. Login successfully.")