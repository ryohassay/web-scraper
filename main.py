# Source: https://qiita.com/yasudaak/items/fee74db16163db3c9af9, https://qiita.com/shin-go/items/291c9d5223d99c185997

from os import read
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random
from time import sleep

CHROME_DRIVER_PATH = 'driver/chromedriver'
FF_DRIVER_PATH = 'driver/geckodriver'
BROWSER_PATH = '/snap/bin/brave'  # For Ubuntu

option = webdriver.ChromeOptions()
option.binary_location = BROWSER_PATH
option.add_argument('--user-data-dir=user')  # Without this line Brave doesn't load the webpages somehow
# option.add_argument('--disable-dev-shm-usage')
# option.add_argument("--incognito")  # OPTIONAL
# option.add_argument("--headless")  # OPTIONAL

# Create new Instance of Chrome
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=option)

# Create new Instance of Firefox
# driver = webdriver.Firefox(executable_path=FF_DRIVER_PATH)


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


def main():
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
    main()