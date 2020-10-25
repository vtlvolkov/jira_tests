from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10)\
            .until(expected_conditions.visibility_of_all_elements_located(locator=self.locator))
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10)\
            .until(expected_conditions.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    def type_text(self, text):
        element = WebDriverWait(self.driver, 10)\
            .until(expected_conditions.element_to_be_clickable(locator=self.locator))
        element.clear()
        element.send_keys(text)
        return None

    def is_present(self):
        try:
            self.find()
        except NoSuchElementException:
            return False
        return True

    @property
    def text(self):
        text = self.web_element.text
        return text

    @property
    def page_title(self):
        title = self.driver.title
        return title
