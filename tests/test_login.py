# import time
# import pytest  # imported from page_utils
from selenium.webdriver.common.keys import Keys

from utils.page_utils import *
import pickle
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import LOGIN_NAME, LOGIN_CODE


# see conftest.py
# this code is left for troubleshooting purposes
# @pytest.fixture(autouse=True)
# def testing():
#     # получение объекта веб-драйвера для нужного браузера в полноэкранном режиме
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--kiosk')
#     pytest.driver = webdriver.Chrome('E:/SF/SeleniumDrivers/chromedriver.exe', chrome_options=chrome_options)
#     # Переходим на страницу авторизации
#     pytest.driver.get(MAINPAGE)
#
#     yield
#     pytest.driver.implicitly_wait(3)
#     pytest.driver.quit()


class TestTryOptions:
    """Testing various social networks login"""

    def test_login_vk(self):
        element_click_by_xpath('//*[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-profile   '
                               'b-header-e-sprite-background"]')
        element = WebDriverWait(pytest.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class ="js-show-soc analytics-click-js"]')))
        element.click()
        element_click_by_xpath('//span[@class ="new-auth__auth-social__text header-sprite new-auth__auth-social_vk"]')
        _ = WebDriverWait(pytest.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="oauth_wrap"]')))
        title = pytest.web_driver.title
        assert title == 'VK | Login'
        pytest.web_driver.back()

    def test_login_schoolmates(self):
        element_click_by_xpath('//*[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-profile   '
                               'b-header-e-sprite-background"]')
        element = WebDriverWait(pytest.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class ="js-show-soc analytics-click-js"]')))
        element.click()
        element_click_by_xpath('//span[@class ="new-auth__auth-social__text header-sprite new-auth__auth-social_ok"]')
        _ = WebDriverWait(pytest.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="ext-widget_cnt js-ext-widget-content"]')))
        title = pytest.web_driver.title
        assert title == 'OK'
        pytest.web_driver.back()

    def test_login_mail_ru(self):
        element_click_by_xpath('//*[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-profile   '
                               'b-header-e-sprite-background"]')
        element = WebDriverWait(pytest.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class ="js-show-soc analytics-click-js"]')))
        element.click()
        element_click_by_xpath('//span[@class ="new-auth__auth-social__text header-sprite '
                               'new-auth__auth-social_mailru"]')
        _ = WebDriverWait(pytest.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="login-panel isMobileApp"]')))
        title = pytest.web_driver.title
        assert title == 'Authorization'
        pytest.web_driver.back()

    def test_login_yandex_google(self):
        """testing link with not refreshing the page"""
        """try yandex"""
        element_click_by_xpath('//*[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-profile   '
                               'b-header-e-sprite-background"]')
        element = WebDriverWait(pytest.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class ="js-show-soc analytics-click-js"]')))
        element.click()
        element_click_by_xpath('//span[@class ="new-auth__auth-social__text header-sprite '
                               'new-auth__auth-social_yandex"]')
        _ = WebDriverWait(pytest.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="passp-flex-wrapper"]')))
        title = pytest.web_driver.title
        assert title == 'Авторизация'
        pytest.web_driver.back()
        # -----------------------------------------------------------------------------------------------------------
        """try goggle"""
        element_click_by_xpath('//*[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-profile   '
                               'b-header-e-sprite-background"]')
        element = WebDriverWait(pytest.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class ="js-show-soc analytics-click-js"]')))
        element.click()
        element_click_by_xpath('//span[@class ="new-auth__auth-social__text header-sprite new-auth__auth-social_gl"]')
        _ = WebDriverWait(pytest.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="initialView"]')))
        assert pytest.web_driver.find_element_by_id('yDmH0d').is_displayed()
        pytest.web_driver.back()


class TestIFLicence:
    def test_login_licence(self):
        """Testing login without the licence"""
        element_click_by_xpath('//*[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-profile   '
                               'b-header-e-sprite-background"]')
        element = WebDriverWait(pytest.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//label[@class="custom-input__input-small"]')))
        element.click()
        button = pytest.web_driver.find_element_by_xpath('//input[@id="g-recap-0-btn"]')
        assert button.get_attribute('value') == "Необходимо принять соглашение"
        element = WebDriverWait(pytest.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//label[@class="custom-input__input-small full-input_wrong"]')))
        element.click()
        button = pytest.web_driver.find_element_by_xpath('//input[@id="g-recap-0-btn"]')
        assert button.get_attribute('value') == "Войти"
        time.sleep(2)
        pytest.web_driver.refresh()

    def test_login_by_wrong_code(self):
        """Testing login with wrong code"""
        my_login = pytest.web_driver.find_element_by_xpath(
            '//*[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-profile   '
            'b-header-e-sprite-background"]')
        my_login.click()  # open login form
        my_login_name = pytest.web_driver.find_element_by_xpath('//*[@class="full-input__input formvalidate-error"]')
        my_login_name.send_keys(Keys.CONTROL + "a")
        my_login_name.send_keys(Keys.DELETE)  # clear field
        my_login_name.send_keys(LOGIN_CODE[:10] + "ABCD")  # enter validation code
        my_login_name.send_keys(Keys.ENTER)
        time.sleep(1)
        element = WebDriverWait(pytest.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//small[@class="full-input__msg-small js-msg-small"]')))

        # element = pytest.web_driver.find_element_by_xpath('//form[@id="auth-by-code"]/div[3]/span[2]/small')
        assert element.text == 'Введенного кода не существует'
        pytest.web_driver.refresh()


class TestMyLogin:
    def test_login(self):
        """Testing execute login and get cookies"""
        my_login = pytest.web_driver.find_element_by_xpath(
            '//*[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-profile   '
            'b-header-e-sprite-background"]')
        my_login.click()  # open login form
        my_login_name = pytest.web_driver.find_element_by_xpath('//*[@class="full-input__input formvalidate-error"]')
        my_login_name.send_keys(Keys.CONTROL + "a")
        my_login_name.send_keys(Keys.DELETE)  # clear field
        # my_login_name.send_keys('alex_tru@list.ru')  # insert e-mail or phone number
        my_login_name.send_keys(LOGIN_NAME)
        btn_login = pytest.web_driver.find_element_by_xpath(
            '//*[@class="new-auth__button js-submit js-submit-by-code new-auth__input full-input__input '
            'new-forms__input_size_m"]')
        btn_login.click()  # submit
        time.sleep(1)
        try:  # in case of sending wrong login name
            my_code = pytest.web_driver.find_element_by_xpath('//input[@class="full-input__input formvalidate-error"]')
            my_code.send_keys(LOGIN_CODE)  # enter validation code
            # print(my_code)
            time.sleep(1)
            pytest.web_driver.find_element_by_xpath('//form[@id="auth-email-sent"]').submit()  # submit form
            time.sleep(10)  # wait for authorisation
        except NoSuchElementException:
            print('\nwrong login name')
        element_click_by_xpath('//span[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-profile   '
                               'b-header-e-sprite-background"]')
        element = pytest.web_driver.find_element_by_xpath('//div[@class="mr10 mt10 mb10"]/span[2]')
        assert element.text[11:] == LOGIN_CODE

        # get cookies
        cookies_list = pytest.web_driver.get_cookies()
        cookiestring = ""
        for cookie in cookies_list[:-1]:
            cookiestring = cookiestring + cookie["name"] + "=" + cookie["value"] + "; "

        cookiestring = cookiestring + cookies_list[-1]["name"] + "=" + cookies_list[-1]["value"]

        # print(cookiestring)
        with open('my_cookies.txt', 'w') as cookiesfile:  # print to file
            print(cookiestring, file=cookiesfile)

        # when login success save cookies using
        pickle.dump(pytest.web_driver.get_cookies(), open("cookies.pkl", "wb"))

    def test_login_by_code(self):
        """Testing login by code"""
        my_login = pytest.web_driver.find_element_by_xpath(
            '//*[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-profile   '
            'b-header-e-sprite-background"]')
        my_login.click()  # open login form
        time.sleep(2)
        my_login_name = pytest.web_driver.find_element_by_xpath('//*[@class="full-input__input formvalidate-error"]')
        my_login_name.send_keys(Keys.CONTROL + "a")
        my_login_name.send_keys(Keys.DELETE)  # clear field
        my_login_name.send_keys(LOGIN_CODE)  # enter validation code
        my_login_name.send_keys(Keys.ENTER)
        time.sleep(10)  # wait for authorisation
        element_click_by_xpath('//span[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-profile   '
                               'b-header-e-sprite-background"]')
        element = pytest.web_driver.find_element_by_xpath('//div[@class="mr10 mt10 mb10"]/span[2]')
        assert element.text[11:] == LOGIN_CODE

    def test_login_confirmation(self):
        """Testing confirmation of the login"""
        my_login = pytest.web_driver.find_element_by_xpath(
            '//*[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-profile   '
            'b-header-e-sprite-background"]')
        my_login.click()  # open login form
        my_login_name = pytest.web_driver.find_element_by_xpath('//*[@class="full-input__input formvalidate-error"]')
        my_login_name.send_keys(Keys.CONTROL + "a")
        my_login_name.send_keys(Keys.DELETE)  # clear field
        my_login_name.send_keys(LOGIN_CODE)  # enter validation code
        my_login_name.send_keys(Keys.ENTER)
        time.sleep(10)  # wait for authorisation
        scroll_to_bottom(pytest.web_driver)
        element_click_by_xpath('//li[@class="b-rfooter-e-item"]/a[@data-event-content="Кабинет"]')
        element = WebDriverWait(pytest.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="cabinet-menu swiper-container-initialized '
                                                      'swiper-container-horizontal '
                                                      'swiper-container-free-mode"]/ul/li[10]')))
        element.click()
        element = WebDriverWait(pytest.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@class="page-contact-info--input '
                                                      'b-form-input-m-verifiable b-form-input readonly             '
                                                      'email-input-personal iforms"]')))
        # print(element.get_attribute('value'))
        assert element.get_attribute('value') == LOGIN_NAME






