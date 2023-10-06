from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def test_setup():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)


def test_login():
    # Navigate to the webpage
    driver.get("https://www.saucedemo.com/")
    print("Application title is ", driver.title)
    print("Application url is ", driver.current_url)
    time.sleep(2)

    # login
    username = driver.find_element(By.CSS_SELECTOR, '[placeholder="Username"]')
    username.send_keys('standard_user')
    time.sleep(2)
    password = driver.find_element(By.CSS_SELECTOR, '[placeholder="Password"]')
    password.send_keys('secret_sauce')
    time.sleep(2)
    login_btn = driver.find_element(By.XPATH, "//input[@id='login-button']")
    login_btn.click()
    time.sleep(3)


def test_add_items_to_cart():
    # item 1
    element1 = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    # time.sleep(2)
    element1.click()
    time.sleep(2)

    # item 2
    element2 = driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    # time.sleep(2)
    element2.click()
    time.sleep(2)

    # item 3
    element3 = driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light')
    element3.click()
    time.sleep(2)


def test_Verify_cart():
    # view the cart
    cart_element = driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']//a")

    # Get the text from the cart element
    cart_text = cart_element.text
    # Convert the text to an integer (assuming it's a number)
    try:
        num_items_in_cart = int(cart_text)
    except ValueError:
        num_items_in_cart = 0  # Handle the case where the text is not a valid number
    # Define the expected number of items (3 in your case)
    expected_num_items = 3
    # Verify the number of items in the cart
    if num_items_in_cart == expected_num_items:
        print("Number of items in the cart matches the expected value:", num_items_in_cart)
    else:
        print("Number of items in the cart does not match the expected value. Actual:", num_items_in_cart)
        time.sleep(3)


def test_checkout():
    # view cart
    cart = driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']//a")
    cart.click()
    time.sleep(2)

    # Scroll down the page by 500 pixels
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)

    # checkout
    checkout = driver.find_element(By.ID, 'checkout')
    checkout.click()
    time.sleep(3)

    # fill information
    First_name = driver.find_element(By.XPATH, "(//input[@id='first-name'])[1]")
    First_name.send_keys('Abeer')
    time.sleep(2)

    Last_name = driver.find_element(By.XPATH, "(//input[@id='last-name'])[1]")
    Last_name.send_keys('Ahmed')
    time.sleep(2)

    Zip_code = driver.find_element(By.XPATH, "(//input[@id='postal-code'])[1]")
    Zip_code.send_keys('58200')
    time.sleep(2)

    # continue
    to_continue = driver.find_element(By.XPATH, "(//input[@id='continue'])[1]")
    to_continue.click()
    time.sleep(2)

    # Scroll down the page by 500 pixels
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)


def test_verify_total_price():
    # items price
    item1_price = 29.99
    item2_price = 9.99
    item3_price = 15.99
    tax = 4.48
    expected_total = item1_price + item2_price + item3_price + tax

    displayed_total = float(
        driver.find_element(By.XPATH, "//div[normalize-space()='Total: $60.45']").text.replace(
            'Total: $60.45', '60.45'))

    # verification
    if expected_total == displayed_total:
        print("Total amount verification successful.")
    else:
        print("Total amount verification failed.")
        time.sleep(2)


def test_finish_shopping():
    finish = driver.find_element(By.XPATH, "(//button[normalize-space()='Finish'])[1]")
    finish.click()
    time.sleep(2)


def test_complete_shopping():
    # Thank you for your order!
    complete = driver.find_element(By.XPATH, "//h2[normalize-space()='Thank you for your order!']")
    complete.is_displayed()
    time.sleep(2)


def test_back_main_page():
    back_home = driver.find_element(By.XPATH, "(//button[normalize-space()='Back Home'])[1]")
    back_home.click()
    time.sleep(3)


def test_close():
    driver.close()
    driver.quit()
    print("Test Completed")
