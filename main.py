# Source: https://qiita.com/yasudaak/items/fee74db16163db3c9af9, https://qiita.com/shin-go/items/291c9d5223d99c185997

import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import random
from time import sleep


def read_txt(path):
    with open(path) as f:
        lines = f.readlines()
    
    return lines


def wait_random(min, max):
    sec = random.uniform(min, max)
    sleep(sec)


def leave_one_tab():
    while(len(driver.window_handles) > 1):
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])


def main(driver):
    google_url = 'https://www.google.com'
    words = read_txt('search_words.txt')

    driver.execute_script("window.open()")  # Open a new tab
    leave_one_tab()

    for word in words:
        word = word.replace('\n' , '')

        driver.execute_script("window.open()")  # Open a new tab
        driver.switch_to.window(driver.window_handles[-1])  # Switch to the last tab
        driver.get(google_url)
        wait = WebDriverWait(driver, 10)  # Wait until the page loads (Max 10s)

        searchbox = driver.find_element_by_name('q')
        searchbox.send_keys(word)
        wait_random(0.3, 1)
        searchbox.send_keys(Keys.RETURN)
        wait = WebDriverWait(driver, 10)
        wait_random(1, 2)
    


if __name__ == '__main__':
    browser = sys.argv[1]
    
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # https://pypi.org/project/webdriver-manager/
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    
    main(driver)
