import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_to_add_to_cart_exist(browser):
    browser.get(link)
    buttons = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(buttons) > 0, f"'There is no button on the page"
    time.sleep(30)
