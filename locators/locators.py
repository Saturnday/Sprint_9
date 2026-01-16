from selenium.webdriver.common.by import By


class SignupPageLocators:

    #1 main page
    BUTTON_GO_TO_CREATE_ACCOUNT = (By.XPATH, "//a[contains(text(),'Создать')]")

    #2 fill up the user form
    INPUT_FIRST_NAME = (By.NAME, "first_name")
    INPUT_LAST_NAME = (By.NAME, 'last_name')
    INPUT_USER_NAME = (By.NAME, 'username')
    INPUT_EMAIL = (By.NAME, 'email')
    INPUT_PASSWORD = (By.NAME, 'password')
    BUTTON_CREATE_ACCOUNT = (By.XPATH, "//button[contains(text(),'Создать')]")

    #3 login page(email,password same as the step 2 "fill up")
    TEXT_ON_PAGE_SIGNIN = (By.XPATH, "//h1[contains(text(),'Войти на сайт')]")
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")

class SigninPageLocators:

    #1 main page
    BUTTON_GO_TO_LOGIN_PAGE = (By.XPATH, "//a[contains(text(),'Войти')]")

    #2 fill up the login form
    INPUT_EMAIL = (By.NAME, 'email')
    INPUT_PASSWORD = (By.NAME, 'password')
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")

    #3 logged in
    BUTTON_LOGOUT = (By.XPATH, "//a[contains(text(),'Выход')]")

class CreateRecipePageLocators:

    #1 Логин
    BUTTON_GO_TO_LOGIN_PAGE = (By.XPATH, "//a[contains(text(),'Войти')]")
    INPUT_EMAIL = (By.NAME, 'email')
    INPUT_PASSWORD = (By.NAME, 'password')
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")

    #2 Создать рецепт
    BUTTON_GO_TO_CREATE_RECIPE = (By.XPATH, "//a[contains(text(),'Создать')]")
    INPUT_NAME = (By.XPATH, "//input[@type='text'][preceding-sibling::div[contains(text(), 'Название')]]")
    CHECKBOX_TAG = (By.XPATH, "//button[following-sibling::span[contains(text(), 'Ужин')]]")
    INPUT_INGREDIENT = (By.XPATH, "//input[@type='text'][preceding-sibling::div[contains(text(), 'Инг')]]")
    SELECT_INGREDIENT = (By.XPATH, "//div[contains(text(),'абрикосовое варенье')]")
    ADD_INGREDIENT = (By.XPATH, "//div[contains(text(), 'Добавить')]")
    INPUT_GRAMS = (By.XPATH, "//div[contains(@class, 'ingredientsAmountInput')]//input")
    INPUT_MINUTES = (By.XPATH, "//div[text()='мин.']/preceding-sibling::*[1]//input")
    INPUT_DESCRIPTION = (By.XPATH, "//textarea[preceding-sibling::div[contains(text(), 'Описание')]]")
    FILE_INPUT = (By.XPATH, "//input[@type='file']")
    #INPUT_PICTURE = (By.XPATH, "//div[@type='button'][contains(text(), 'Выбрать')]")
    BUTTON_CREATE = (By.XPATH, "//button[contains(text(),'Создать')]")
    
    #2 Проверка
    CHECK_CARD_LOADED = (By.XPATH, "//img[contains(@class, 'single-card__image')]")
    CHECK_NAME = (By.XPATH, "//h1[contains(@class, 'card__title')]")
    BUTTON_LOGOUT = (By.XPATH, "//a[contains(text(),'Выход')]")

    












class _LoginPageLocators:
    INPUT_EMAIL = (By.NAME, "name")
    INPUT_PASSWORD = (By.NAME, 'Пароль')
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(),'Войти')]")
    LINK_RESTORE_PASSWORD = (By.XPATH, '//a[text()="Восстановить пароль"]')
    BUTTON_RESTORE = (By.XPATH, '//button[text()="Восстановить"]')
    TEXT_RESTORE = (By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")
    SHOW_PASSWORD = (By.CSS_SELECTOR, "div[class='input__icon input__icon-action'] svg")
    INPUT_NEW_PASSWORD = (By.XPATH, '//input[@name="Введите новый пароль"]')
    PASSWORD = (By.XPATH, '//label[contains(text(), "Пароль")]/parent::div')
    OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")

class MainPageLocators:
    BUTTON_CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')
    BUTTON_ORDER_FEED = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')
    INGREDIENT_ITEM = (By.XPATH, '//p[text()="Соус фирменный Space Sauce"]')  
    ORDER_COUNTER = (By.XPATH, '//span[@class="counter_counter__num__3nV4z"]')
    READY_ORDERS_COUNTER = (By.XPATH, '//p[contains(text(),"Выполнено за все время")]')
    BUTTON_PROFILE = (By.XPATH, '//p[text()="Личный Кабинет"]')
    OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")
    NAME = (By.XPATH, "//label[contains(text(),'Имя')]")
    BUTTON_PROFILE = (By.XPATH, '//p[text()="Личный Кабинет"]')
    BUTTON_ORDER_HISTORY = (By.XPATH, '//a[text()="История заказов"]')
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(),'Выход')]")
    ORDERS_READY = (By.XPATH, "//p[contains(text(),'Готовы:')]")
    LINK_RESTORE_PASSWORD = (By.XPATH, '//a[text()="Восстановить пароль"]')
    FEED = (By.CLASS_NAME, 'OrderFeed_orderList__cBvyi')

    BUNS = (By.XPATH, "//span[text()='Булки']")
    # Соусы
    SAUCES = (By.XPATH, "//span[text()='Соусы']")
    # Начинки
    FILLINGS = (By.XPATH, "//span[text()='Начинки']")

    INGREDIENTS = (By.CSS_SELECTOR, "a.BurgerIngredient_ingredient_1TVf6")
    INGREDIENT_MODAL = (By.CSS_SELECTOR, "div.Modal_modal_opened__3ISw4")
    BUTTON_CLOSE_MODAL = (By.CSS_SELECTOR, "button.Modal_modal__close")
    INGREDIENT_LINKS = (By.CSS_SELECTOR, "a.BurgerIngredient_ingredient_1TVf6")
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//div[contains(@class,'Modal') or contains(@class,'modal')]//h2")
    INGREDIENT_MODAL_CLOSE = (By.TAG_NAME, "button")
    
    BUN_1 = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    BUN_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")

    ELEMENT_TO = (By.XPATH, "//span[contains(text(), 'Перетяните булочку сюда')]")

    @classmethod
    def ingredient_by_name(cls, name):
        return By.XPATH, f"//p[contains(text(), '{name}')]"
    
    @classmethod
    def get_ingredient_locator(cls, ingredient_name):
        return (By.XPATH, f"//span[text()='{ingredient_name}']")
    
    @classmethod
    def counter_by_ingredient_name(cls, name):
        return By.XPATH, (
            f"//p[contains(text(), '{name}')]/ancestor::a"
            f"//p[contains(@class, 'counter_counter__num')]"
        )

    BUTTON_MAKE_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить')]")
    ORDER_IN_PROCESS = (By.XPATH, "//p[contains(text(), 'готовить')]")
    LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")
    ORDER_NUMBER = (By.XPATH, "//p[text()='идентификатор заказа']/preceding-sibling::h2")
    CLOSER_ORDER = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK")
    CLOSE_ORDER_WINDOW_BUTTON = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//button")


class ProfilePageLocators:
    BUTTON_PROFILE = (By.XPATH, "//a[@href='/account/profile']")
    BUTTON_ORDER_HISTORY = (By.XPATH, "//a[@href='/account/order-history']")
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")
    
class FeedPageLocators:
    FEED_ORDER_ITEM = (By.CLASS_NAME, 'OrderHistory_link__1iNby')
    FEED_ORDER_MODAL = (By.XPATH, '//p[contains(text(), "Cостав")]')
    ALL_ORDER_NUMBERS = (By.CSS_SELECTOR, 'a.order-card span.number, div.order-card span.number')
    COUNTER_TOTAL_DONE = (By.CSS_SELECTOR, 'p.total-done, #total-done')
    COUNTER_TODAY_DONE = (By.XPATH, '//p[contains(text(), "Выполнено за сегодня")]/following-sibling::p')
    FEED = (By.CLASS_NAME, 'OrderFeed_orderList__cBvyi')
    IN_WORK_ORDER_NUMBERS = (By.XPATH, "//p[contains(text(), 'В работе')]/following-sibling::ul[2]/li")