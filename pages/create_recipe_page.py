import allure
from pathlib import Path
from data.data import TestData
from pages.base_page import BasePage
from locators.locators import CreateRecipePageLocators

class CreateRecipe(BasePage):

    URL = f"{TestData.BASE_URL}/recipes"

    @allure.step("Открыть главную страницу")
    def open(self):
        self.open_url(self.URL)
    
    @allure.step("Войти в акканут")
    def login(self):
        self.click(CreateRecipePageLocators.BUTTON_GO_TO_LOGIN_PAGE)
        self.find_element(CreateRecipePageLocators.INPUT_EMAIL).send_keys(TestData.EXISTING_EMAIL)
        self.find_element(CreateRecipePageLocators.INPUT_PASSWORD).send_keys(TestData.EXISTING_PASSWORD)
        self.click(CreateRecipePageLocators.BUTTON_LOGIN)
        self.find_element(CreateRecipePageLocators.BUTTON_LOGOUT)

    @allure.step("Создать рецепт")
    def create_recipe(self):

        self.find_element(CreateRecipePageLocators.BUTTON_GO_TO_CREATE_RECIPE)
        self.click(CreateRecipePageLocators.BUTTON_GO_TO_CREATE_RECIPE)
        URL = f"{TestData.BASE_URL}/recipes/create"
        self.open_url(URL)
        self.wait_for_page_ready()

        name = TestData.VALID_RECIPE['name']

        self.find_element(CreateRecipePageLocators.INPUT_NAME).send_keys(name)
        self.find_element(CreateRecipePageLocators.CHECKBOX_TAG).click()

        # Add ingredient
        ingredient_input = self.find_element(CreateRecipePageLocators.INPUT_INGREDIENT)
        ingredient_input.send_keys(TestData.VALID_RECIPE['ingredient'])
        self.find_element(CreateRecipePageLocators.SELECT_INGREDIENT).click()
        self.click(CreateRecipePageLocators.INPUT_GRAMS)
        self.find_element(CreateRecipePageLocators.INPUT_GRAMS).send_keys(TestData.VALID_RECIPE['amount'])
        self.find_element(CreateRecipePageLocators.ADD_INGREDIENT).click()

        self.find_element(CreateRecipePageLocators.INPUT_MINUTES).send_keys(TestData.VALID_RECIPE['time'])

        # Fill in description
        self.find_element(CreateRecipePageLocators.INPUT_DESCRIPTION).send_keys(TestData.VALID_RECIPE['description'])

        # Upload picture
        self.upload_picture()

        self.find_element(CreateRecipePageLocators.BUTTON_CREATE).click()

        return name

    @allure.step("Загрузка изображения")
    def upload_picture(self, filename="pic.jpeg"):

        print(self.driver.page_source)
        project_root = Path(__file__).parent.parent
        file_path = project_root / "assets" / filename
        file_input = self.find_present_element(CreateRecipePageLocators.FILE_INPUT)
        self.driver.execute_script("arguments[0].style.display = 'block';", file_input)
        file_input.send_keys(str(file_path))
    
    @allure.step("Проверить: загрузилась ли форма")
    def check_recipe_loaded(self):
        return self.find_element(CreateRecipePageLocators.CHECK_CARD_LOADED)

    @allure.step("Проверить: название рецепта")
    def check_order_name(self):
        return self.find_element(CreateRecipePageLocators.CHECK_NAME).text

