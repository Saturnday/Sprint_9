import pytest
import allure
from pages.create_recipe_page import CreateRecipe


@allure.suite("Создание рецепта")
class TestCreateRecipe:

    @allure.step("Проверка успешного создания рецепта")
    def test_create_recipe_success(self, driver):

        recipe_page = CreateRecipe(driver)
        recipe_page.open()
        recipe_page.login()
        name = recipe_page.create_recipe()

        with allure.step("Проверить, что рецепт создан"):
            assert name == recipe_page.check_order_name()