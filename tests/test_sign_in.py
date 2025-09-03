import pytest
import allure
from pages.sing_in_page import SignIn


@allure.suite("Вход в аккаунт под существующим пользователем")
class TestSignIn:

    @allure.step("Войти в аккаунт")
    def test_sing_in_succesfull(self, driver):
        sing_in = SignIn(driver)
        sing_in.open()

        sing_in.open_login_page()
        sing_in.login()


        assert sing_in.login_was_successful() and sing_in.is_signin_page_opened()