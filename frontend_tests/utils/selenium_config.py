from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.logger import get_logger

logger = get_logger()

def get_web_driver():
    logger.info("Creation of web driver for Chrome is starting.")

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=1920,1080")

    import tempfile
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    driver = webdriver.Chrome(options=options)

    logger.info("Creation of web driver was ended.")
    return driver
