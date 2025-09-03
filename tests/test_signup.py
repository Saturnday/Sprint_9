import pytest
import allure
from pages.signup_page import Signup


@allure.suite("Создать пользователя и войти в аккаунт")
class TestSignup:

    @allure.step("Создать пользователя")
    def test_create_user(self, driver):
        login = Signup(driver)
        login.open()
        login.open_registration_page()
        login.create_account()

        assert login.sign_in_page_opened()
        assert login.is_signin_page_opened()


    