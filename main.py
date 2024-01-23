from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

number_telephone = '89384293264'
gmail = "zimarev.nazar13@gmail.com"
name = 'Назар'
surname = 'Сикорски'
birth_date = '30072002'
password = 'Z1mar3v13'
phone = "9384293264"

# Путь к драйверу браузера. Убедитесь, что у вас установлен и указан правильный путь.
driver_path = "/Users/nazarzimarev/Desktop/SberMegaAccounts/chromedriver_mac64/chromedriver"

# Опции для браузера Chrome
chrome_options = webdriver.ChromeOptions()

# Отключение запросов на уведомления
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Инициализация веб-драйвера (в данном случае используем Chrome)
driver = webdriver.Chrome(options=chrome_options)

# Открытие сайта
driver.get("https://megamarket.ru/login/")

# Подождем 10 секунд (можете изменить это значение по вашему усмотрению)
time.sleep(10)

# Найдем кнопку "Войти по номеру телефона" по классу и кликнем по ней
login_button = driver.find_element(By.CLASS_NAME, "auth-main__phone-login")
login_button.click()

# Подождем еще 60 секунд
time.sleep(15)

phone_input = driver.find_element(By.CLASS_NAME, "text-input")
time.sleep(2)
phone_input.send_keys(phone)

time.sleep(15)

# Найдем кнопку "Получить код" по классу и кликнем по ней
get_code_button = driver.find_element(By.CLASS_NAME, "login-form__submit")
get_code_button.click()

# ждём перед получением кода
time.sleep(50)

driver.get('https://megamarket.ru/personal/loyalty')

time.sleep(10)

# Подождем, пока кнопка "Создать Сбер ID" станет видимой (максимум 10 секунд)
try:
    create_sber_id_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.sbid-button span.sbid-button__text"))
    )

    # Используем JavaScript для выполнения клика
    driver.execute_script("arguments[0].click();", create_sber_id_button)
except Exception as e:
    print(f"Не удалось найти и нажать на кнопку: {e}")

'''time.sleep(30)

create_sber_id_button = driver.find_element(By.CLASS_NAME, "sbid-button__text")
create_sber_id_button.click()'''

time.sleep(30)

# Ждем, пока поле ввода станет видимым и активным
phone_input = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="phoneNumber-input"][type="tel"]'))
)

# Используем ActionChains для ввода текста в поле
ActionChains(driver).move_to_element(phone_input).click().send_keys(phone).perform()

time.sleep(10)

# Найдем кнопку "Продолжить" по атрибуту data-testid и кликнем по ней
continue_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="phoneNumber-nextButton"][type="submit"]')
continue_button.click()

time.sleep(30)

first_name_input = driver.find_element(By.NAME, 'firstName')
first_name_input.send_keys(name)  # Замените 'Ваше_имя' на фактическое имя
time.sleep(2)
last_name_input = driver.find_element(By.NAME, 'lastName')
last_name_input.send_keys(surname)  
time.sleep(2)
# Дата рождения
dob_input = driver.find_element(By.NAME, 'dob')
dob_input.send_keys(birth_date)  
time.sleep(2)
# Пароль
dpassword_input = driver.find_element(By.NAME, 'password')
dpassword_input.send_keys(password)  
time.sleep(2)
# Подтверждение пароля
dpassword_confirm_input = driver.find_element(By.NAME, 'confirmPassword')
dpassword_confirm_input.send_keys(password)  
time.sleep(2)
email_conf = driver.find_element(By.NAME, 'email')
email_conf.send_keys(gmail)
time.sleep(3)
# Найдем кнопку по тексту "Создать Сбер ID" и выполним клик
create_sber_id_button = driver.find_element(By.XPATH, '//button[contains(.,"Создать Сбер ID")]')
create_sber_id_button.click()

time.sleep(30)

# Закрытие браузера
driver.quit()


