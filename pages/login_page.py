from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.locator import Locator


class LoginPage(BasePage):

    @property
    def login_field(self):
        locator = Locator(By.ID, 'login-form-username')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def password_field(self):
        locator = Locator(By.ID, 'login-form-password')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def login_button(self):
        locator = Locator(By.ID, 'login')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def login_again_link(self):
        locator = Locator(By.XPATH, '//a[contains(text(), "Log in again.")]')
        return BaseElement(driver=self.driver, locator=locator)

    def do_login(self):
        self.go()
        self.login_field.type_text('botulizmer')
        self.password_field.type_text('qwerty')
        self.login_button.click()
        return None


