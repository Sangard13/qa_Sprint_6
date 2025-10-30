from selenium.webdriver.common.by import By


class MainLocators:
    # Кнопки заказа
    HEADER_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать'")
    FOOTER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__3TSOI')]")

    # Вопросы о важном
    QUESTION = (By.ID, "accordion__heading-{}")
    ANSWER = (By.ID, "accordion__panel-{}")