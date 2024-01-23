from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def open_browser():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def login_to_megamarket(driver, phone):
    driver.get("https://megamarket.ru/login/")
    time.sleep(7)
    login_button = driver.find_element(By.CLASS_NAME, "auth-main__phone-login")
    login_button.click()
    time.sleep(7)
    phone_input = driver.find_element(By.CLASS_NAME, "text-input")
    time.sleep(2)
    phone_input.send_keys(phone)
    time.sleep(15)
    get_code_button = driver.find_element(By.CLASS_NAME, "login-form__submit")
    get_code_button.click()
    wait = WebDriverWait(driver, 500)
    wait.until(EC.url_to_be('https://megamarket.ru/'))
    driver.get('https://megamarket.ru/personal/loyalty')

def create_sber_id(driver, phone, name, surname, birth_date, password, gmail):
    try:
        create_sber_id_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.sbid-button span.sbid-button__text"))
        )
        driver.execute_script("arguments[0].click();", create_sber_id_button)
    except Exception as e:
        print(f"Не удалось найти и нажать на кнопку: {e}")

    time.sleep(30)
    phone_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="phoneNumber-input"][type="tel"]'))
    )
    ActionChains(driver).move_to_element(phone_input).click().send_keys(phone).perform()
    time.sleep(10)
    continue_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="phoneNumber-nextButton"][type="submit"]')
    continue_button.click()
    time.sleep(30)
    first_name_input = driver.find_element(By.NAME, 'firstName')
    first_name_input.send_keys(name)
    time.sleep(2)
    last_name_input = driver.find_element(By.NAME, 'lastName')
    last_name_input.send_keys(surname)
    time.sleep(2)
    dob_input = driver.find_element(By.NAME, 'dob')
    dob_input.send_keys(birth_date)
    time.sleep(2)
    dpassword_input = driver.find_element(By.NAME, 'password')
    dpassword_input.send_keys(password)
    time.sleep(2)
    dpassword_confirm_input = driver.find_element(By.NAME, 'confirmPassword')
    dpassword_confirm_input.send_keys(password)
    time.sleep(2)
    email_conf = driver.find_element(By.NAME, 'email')
    email_conf.send_keys(gmail)
    time.sleep(3)
    create_sber_id_button = driver.find_element(By.XPATH, '//button[contains(.,"Создать Сбер ID")]')
    create_sber_id_button.click()
    time.sleep(20)
    # Найдем элемент с использованием XPath
    check_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//svg[@class="svg-icon"]'))
    )

    # Выполним клик по найденному элементу
    check_button.click()
    time.sleep(5)
    # Найдем элемент кнопки с использованием XPath
    join_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="btn profile-loyalty-no-join-program__button"]'))
    )

    # Выполним клик по найденному элементу
    join_button.click()

def main():
    number_telephone = '89384293264'
    gmail = "vlasovay4041@rambler.ru"
    name = 'Александр'
    surname = 'Мершин'
    birth_date = '30072002'
    password = 'Vasgen43!'
    phone = "9776302425"

    driver = open_browser()
    login_to_megamarket(driver, phone)
    create_sber_id(driver, phone, name, surname, birth_date, password, gmail)
    driver.quit()

if __name__ == "__main__":
    main()
