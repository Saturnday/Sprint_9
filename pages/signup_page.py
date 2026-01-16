import allure
from data.data import TestData
from pages.base_page import BasePage
from locators.locators import SignupPageLocators

class Signup(BasePage):

    URL = TestData.BASE_URL

    @allure.step("Открыть главную страницу")
    def open(self):
        self.open_url(self.URL)
    
    @allure.step("Открыть форму регистрации")
    def open_registration_page(self):
        self.click(SignupPageLocators.BUTTON_GO_TO_CREATE_ACCOUNT)

    @allure.step("Создать аккаунт [Имя Фамилия Ник Имейл Пароль]")
    def create_account(self):

        self.find_element(SignupPageLocators.INPUT_FIRST_NAME).send_keys(TestData.VALID_USER['first_name'])
        self.find_element(SignupPageLocators.INPUT_LAST_NAME).send_keys(TestData.VALID_USER['last_name'])
        self.find_element(SignupPageLocators.INPUT_USER_NAME).send_keys(TestData.VALID_USER['user_name'])
        self.find_element(SignupPageLocators.INPUT_EMAIL).send_keys(TestData.VALID_USER['email'])
        self.find_element(SignupPageLocators.INPUT_PASSWORD).send_keys(TestData.VALID_USER['password'])

        self.find_element(SignupPageLocators.BUTTON_CREATE_ACCOUNT).click()

    @allure.step("Проверка страница авторизации содержит нужные элементы")
    def sign_in_page_opened(self):
        return self.find_element(SignupPageLocators.TEXT_ON_PAGE_SIGNIN)
    
    @allure.step("Проверяет, что мы на странице авторизации")
    def is_signin_page_opened(self):
        return "signin" in self.get_current_url()
    


    
    
