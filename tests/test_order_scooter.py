import pytest
import allure
import time
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import OrderData


class TestOrderScooter:

    @allure.title('Заказ самоката: {user_data[name]} через {button_type} кнопку')
    @pytest.mark.parametrize('button_type,user_data', [
        ('top', OrderData.USER_1),
        ('bottom', OrderData.USER_2)
    ])
    def test_order_scooter(self, driver, button_type, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.click_order_btn(button_type)
        order_page.fill_first_page(user_data)
        order_page.fill_second_page(user_data)
        order_page.wait_for_confirmation()
        order_page.click_confirm_order_modal()

        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message

    @allure.title("Проверка перехода по логотипу Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_scooter_logo()

        assert main_page.is_main_page()

    @allure.title("Проверка перехода по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_window = driver.current_window_handle
        main_page.click_yandex_logo()

        main_page.wait.until(lambda driver: len(driver.window_handles) > 1)
        new_window = [window for window in driver.window_handles if window != main_window][0]
        driver.switch_to.window(new_window)

        main_page.wait.until(lambda driver: "dzen.ru" in driver.current_url)
        current_url = driver.current_url

        driver.close()
        driver.switch_to.window(main_window)

        assert "dzen.ru" in current_url