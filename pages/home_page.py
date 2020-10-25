from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.locator import Locator


class HomePage(BasePage):

    @property
    def page_header(self):
        locator = Locator(By.XPATH, "//h1[contains(text(),'System Dashboard')]")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def user_avatar(self):
        locator = Locator(By.CLASS_NAME, "aui-avatar-inner")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def logout_link(self):
        locator = Locator(By.ID, "log_out")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )