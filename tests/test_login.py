from pytest import mark

from pages.login_page import LoginPage
from pages.home_page import HomePage


@mark.smoke
class LoginTest:
    def test_correct_login(self, chrome_browser):
        login_page = LoginPage(driver=chrome_browser)
        login_page.go()
        login_page.login_field.type_text('botulizmer')
        login_page.password_field.type_text('qwerty')
        login_page.login_button.click()
        home_page = HomePage(driver=chrome_browser)
        assert home_page.user_avatar.is_present()

    def test_logout(self, chrome_browser):
        login_page = LoginPage(driver=chrome_browser)
        login_page.do_login()
        home_page = HomePage(driver=chrome_browser)
        home_page.user_avatar.click()
        home_page.logout_link.click()
        assert login_page.login_again_link.is_present()

