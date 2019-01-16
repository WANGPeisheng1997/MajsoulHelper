from selenium import webdriver


def web_init():
    driver = webdriver.PhantomJS(executable_path='E:/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
    return driver


def web_close(driver):
    driver.quit()


def open_url(driver, url):
    driver.get(url)
    source = driver.page_source
    return source