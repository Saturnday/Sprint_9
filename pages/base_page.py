from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу по URL")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Клик по элементу с ожиданием")
    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Найти элемент с ожиданием")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Найти элементы с ожиданием")
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step("Ожидание исчезновения элемента")
    def wait_until_not_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until_not(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Ждать загрузки страницы')
    def wait_for_page_ready(self, timeout=15):

        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    @allure.step('Найти элемент')
    def find_present_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
