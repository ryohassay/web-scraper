# Source: https://qiita.com/yasudaak/items/fee74db16163db3c9af9, https://qiita.com/shin-go/items/291c9d5223d99c185997

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

CHROME_DRIVER_PATH = '/home/ryoji/dev/personal/web-scraper/driver/chromedriver'
FF_DRIVER_PATH = '/home/ryoji/dev/personal/web-scraper/driver/geckodriver'
BROWSER_PATH = '/snap/bin/brave'

option = webdriver.ChromeOptions()
option.binary_location = BROWSER_PATH
option.add_argument('--user-data-dir=user')  # Without this line Brave doesn't load the webpages somehow
# option.add_argument('--disable-dev-shm-usage')
# option.add_argument("--incognito")  # OPTIONAL
# option.add_argument("--headless")  # OPTIONAL

# Create new Instance of Chrome
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=option)
# driver = webdriver.Firefox(executable_path=FF_DRIVER_PATH)


def read_txt(path):
	with open(path) as f:
		lines = f.readlines()
	
	return lines


def main():
	urls = read_txt('urls.txt')

	for url in urls:
		driver.execute_script("window.open()")  # Open a new tab
		driver.switch_to.window(driver.window_handles[-1])  # Switch to the last tab
		driver.get(url)
		wait = WebDriverWait(driver, 10)  # Wait until the page loads (Max 10s)
	


if __name__ == '__main__':
    main()