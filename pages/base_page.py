class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://localhost:8080'

    def go(self):
        self.driver.get(self.base_url)


