import time
import os
import csv
import json

from utils import config
from utils import selenium_login
from utils import selenium_response_timer
from utils import selenium_response_text
from utils import selenium_config
from utils.logger import get_logger

logger = get_logger()

def main():
    try:
        driver = selenium_config.get_web_driver()
        driver.get(config.CHATBOT_URL)

        logger.info("Selenium login process was sterted.")
        
        selenium_login.login(driver)
        
        logger.info("Selenium response timer process was started.")
        
        sentences = read_input_file()
        
        for sentence in sentences:
            response_text = selenium_response_text.get_response_text(driver, sentence)
            log_response_text(sentence, response_text)

    except Exception as e:
        logger.error("Error occured:" + e)

    finally:
        logger.info("Selenium responce time process was ended.")
        time.sleep(config.END_WAITING_TIME)
        driver.quit()

        
def read_input_file():
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, "inputs", "test_dataset.json")
    
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    return [item["question"] for item in data if "question" in item]


def log_response_text(sentence, response_text):
    logs_dir = os.path.join(os.path.dirname(__file__), "logs")
    os.makedirs(logs_dir, exist_ok=True)
    file_path = os.path.join(logs_dir, "response_texts.csv")

    write_header = not os.path.exists(file_path)

    with open(file_path, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        
        if write_header:
            writer.writerow(["sentence", "response"])
            
        writer.writerow([sentence, response_text])


if __name__ == "__main__":
    main()
