import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger()

def get_response_text(driver, message):
    logger.info("Response timer is starting. Message: " + message)
    
    chat_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))

    send_button = driver.find_element(By.XPATH, "//button[contains(@class, 'ant-btn-primary')]")

    chat_input.send_keys(message)

    WebDriverWait(driver, 10).until(lambda d: send_button.is_enabled())

    start_time = time.time()

    send_button.click()

    initial_message_count = len(driver.find_elements(By.XPATH, "//div[contains(@class, 'message-container')]//span[contains(@class, 'message-text')]"))

    WebDriverWait(driver, 30).until(
        lambda d: len(d.find_elements(By.XPATH, "//div[contains(@class, 'message-container')]//span[contains(@class, 'message-text')]")) > initial_message_count
    )

    messages = driver.find_elements(By.XPATH, "//div[contains(@class, 'message-container')]//span[contains(@class, 'message-text')]")

    response_text = messages[-1].text

    logger.info("Response timer was ended. " + f"Response of the chatbot: {response_text}")
    
    return response_time