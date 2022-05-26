import time
import pytest
import os
import pickle

from selenium import webdriver  # подключение библиотеки
from data import MAINPAGE  # get url address
from data import LOGIN_CODE


@pytest.fixture(scope="function", autouse=True)
def testing():
    # # получение объекта веб-драйвера для нужного браузера в полноэкранном режиме
    # # если нет внешнего драйвера и этот тест запускается отдельно
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--kiosk')
    # pytest.web_driver = webdriver.Chrome('F:/SF/SeleniumDrivers/chromedriver.exe', chrome_options=chrome_options)
    # pytest.web_driver.get(MAINPAGE)
    # prepare cookies
    time.sleep(3)
    if os.path.exists('cookies.pkl'):
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            pytest.web_driver.add_cookie(cookie)
        pytest.web_driver.refresh()  # login with cookies
        time.sleep(3)

    yield
    pytest.web_driver.implicitly_wait(3)
    # # если нет внешнего драйвера и этот тест запускается отдельно
    # pytest.web_driver.quit()


def test_login_cookies():  # execute login with cookies
    my_login = pytest.web_driver.find_element_by_xpath(
        '//*[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-profile   b-header-e-sprite-background"]')
    my_login.click()
    element = pytest.web_driver.find_element_by_xpath('//div[@class="mr10 mt10 mb10"]/span[2]')
    assert element.text[11:] == LOGIN_CODE
