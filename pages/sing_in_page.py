import allure
from data.data import TestData
from pages.base_page import BasePage
from locators.locators import SigninPageLocators

class SignIn(BasePage):

    URL = TestData.BASE_URL

    @allure.step("Открыть главную страницу")
    def open(self):
        self.open_url(self.URL)

    @allure.step("Открыть страницу логина")
    def open_login_page(self):
        self.click(SigninPageLocators.BUTTON_GO_TO_LOGIN_PAGE)
    
    @allure.step("Войти в акканут")
    def login(self):
        self.find_element(SigninPageLocators.INPUT_EMAIL).send_keys(TestData.EXISTING_EMAIL)
        self.find_element(SigninPageLocators.INPUT_PASSWORD).send_keys(TestData.EXISTING_PASSWORD)
        self.click(SigninPageLocators.BUTTON_LOGIN)

    @allure.step("Проверка логин успешен")
    def login_was_successful(self):
        return self.find_element(SigninPageLocators.BUTTON_LOGOUT)
    
    @allure.step("Проверяет, что мы на главной странице")
    def is_signin_page_opened(self):
        return "recipes" in self.get_current_url()