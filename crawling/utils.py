import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_element(driver, css_selector):
    return driver.find_element(By.CSS_SELECTOR, css_selector)

def find_elements(driver, css_selector):
    return driver.find_elements(By.CSS_SELECTOR, css_selector)

def waiting_element(driver, css_selector, time=5):
    return WebDriverWait(driver, time).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )

def save_csv(data, path):
    pd.DataFrame(data).to_csv(path, header=True, index=False, encoding='utf-8-sig')