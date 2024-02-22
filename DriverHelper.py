import logging
import time
from selenium.webdriver.common.by import By
from collections import OrderedDict
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_element(_driver, _xpath):
    logging.info("clickElement: " + _xpath)
    wait = WebDriverWait(_driver, 20)
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, _xpath)))
        element.click()
    except Exception as e:
        logging.error("clickElement error: " + _xpath)
        print(e)
    time.sleep(1)


def input_element(_driver, _xpath, _text):
    logging.info("inputElement: " + _xpath)
    try:
        element = _driver.find_element(By.XPATH, _xpath)
        element.send_keys(_text)
    except Exception as e:
        logging.error("inputElement error: " + _xpath)
        print(e)


def get_element_text(_driver, _xpath):
    logging.info("getElementText: " + _xpath)
    try:
        element = _driver.find_element(By.XPATH, _xpath)
        if element.text == "" or element.text == None:
            return element.get_attribute("textContent") or ""
        return element.text
    except Exception as e:
        logging.error("getElementText error: " + _xpath)
        print(e)
        return ""


def wait_until_element_clickable(_driver, _xpath, timeout=20, waitText=None):
    times = 0
    while True:
        time.sleep(1)
        try:
            logging.info("waitUntilElementClickable: " + _xpath)
            print("Friends, here! More info: " + waitText)
            _driver.find_element(By.XPATH, _xpath).click()
            break
        except Exception as e:
            logging.error("waitUntilElementClickable waiting for: " + _xpath)
            pass
        times += 1
        if times > timeout:
            break