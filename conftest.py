from pytest import fixture

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@fixture(scope='function')
def chrome_browser():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    yield browser

