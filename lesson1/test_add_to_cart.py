from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_add_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    first_item_text_before = driver.find_element(By.XPATH, "//div [contains( text(), 'Sauce Labs Backpack')]").text

    add_to_cart_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    cart_icon_link = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    cart_icon_link.click()

    first_item_text_after = driver.find_element(By.XPATH, "//div [contains( text(), 'Sauce Labs Backpack')]").text

    assert first_item_text_before == first_item_text_after



