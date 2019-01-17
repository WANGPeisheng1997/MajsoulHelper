import time
from selenium import webdriver


def web_init():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/Google/Chrome/Application/chromedriver",
                               chrome_options=chrome_options)
    return driver


def web_close(driver):
    driver.quit()


def open_url(driver, url):
    now = time.time()
    driver.get(url)
    source = driver.page_source
    print(time.time() - now)
    return source