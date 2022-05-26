from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from utils.page_utils import *
from data import MAINPAGE

"""This tests are checking the logic of Labirint web page without login in
    tests can be run as file:   python -m pytest -v .\tests\test_logic_no_login.py
    or as separate test:   python -m pytest -v .\tests\test_logic_no_login.py -k any_class
    or couple of tests:   python -m pytest -v .\tests\test_logic_no_login.py -k 'test_1 or test_2'
    """


# see conftest.py
# this code is left for troubleshooting purposes
# @pytest.fixture(scope="session", autouse=True)
# def testing():
#     # получение объекта веб-драйвера для нужного браузера в полноэкранном режиме
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--kiosk')
#     pytest.web_driver = webdriver.Chrome('F:/SF/SeleniumDrivers/chromedriver.exe', chrome_options=chrome_options)
#     pytest.web_driver.get(MAINPAGE)
#
#     yield
#     pytest.web_driver.implicitly_wait(3)
#     pytest.web_driver.quit()

@pytest.fixture(scope="function", autouse=True)
def main_page():
    """Returns to main page after each test"""
    yield
    pytest.web_driver.get(MAINPAGE)


class TestMoveToBasket:  # Testing cart
    def test_move_book_to_basket(self):
        """From books menu add a book to the cart"""
        basket_before = check_basket(pytest.web_driver)
        element = pytest.web_driver.find_element_by_xpath(
            '//a[@href="/books/"]')
        element.click()
        pytest.web_driver.implicitly_wait(2)
        element = pytest.web_driver.find_element_by_xpath(
            '//a[@href="/genres/1850/"]')
        element.click()
        element = pytest.web_driver.find_elements_by_xpath(
            '//div[@class ="card-column card-column_gutter col-xs-3 col-sm-2"]')[0]
        element.click()
        element = pytest.web_driver.find_element_by_xpath(
            '//a[@class="btn btn-small btn-primary btn-buy"]')
        element.click()
        time.sleep(2)
        basket_after = check_basket(pytest.web_driver)
        # check if item is added
        assert (basket_after - basket_before) == 1

    def test_move_together_to_basket(self):
        """Adds a pack of books to the cart"""
        basket_before = check_basket(pytest.web_driver)
        element = pytest.web_driver.find_element_by_xpath(
            '//a[@href="/books/"]')
        element.click()
        pytest.web_driver.implicitly_wait(2)
        element = pytest.web_driver.find_element_by_xpath(
            '//a[@href="/genres/1850/"]')
        element.click()
        element = pytest.web_driver.find_elements_by_xpath(
            '//div[@class ="card-column card-column_gutter col-xs-3 col-sm-2"]')[0]
        element.click()
        elements = pytest.web_driver.find_elements_by_xpath(
            '//div[@class="buyto-checkers"]/div')
        books_in_pack = len(elements)
        hover_move_click(pytest.web_driver, '//*[@id="buyto-buyids"]')
        # element = pytest.web_driver.find_element_by_xpath(
        #     '//div[@id="buy-together"]/div/a[@id="buyto-buyids"]')
        # element.click()
        time.sleep(2)
        basket_after = check_basket(pytest.web_driver)
        # check if items pack is added
        assert (basket_after - basket_before) == books_in_pack

    def test_move_from_best_to_basket(self):
        """Adds a pack of best books to the cart"""
        basket_before = check_basket(pytest.web_driver)
        element = pytest.web_driver.find_element_by_xpath(
            '//span[@class="b-header-b-menu-e-link"]/a[@href="/best/"]')
        element.click()
        pytest.web_driver.implicitly_wait(2)
        element = pytest.web_driver.find_element_by_xpath(
            '//li/a[@href="/best/giftbooks/"]')
        element.click()
        element = pytest.web_driver.find_element_by_xpath(
            '//div[@class="jcarousel-items jcarousel-items-rating"]/div[1]/div/div/div/a/img')
        element.click()
        elements = pytest.web_driver.find_elements_by_xpath(
            '//div[@class="buyto-checkers"]/div')
        books_in_pack = len(elements)
        # hover_move_click(pytest.web_driver, '//*[@id="buyto-buyids"]')
        time.sleep(2)
        element = pytest.web_driver.find_element_by_xpath(
            '//div[@class="buy-together__btn-wrap"]/a')
        element.click()
        time.sleep(2)
        basket_after = check_basket(pytest.web_driver)
        # check if items pack is added
        assert (basket_after - basket_before) == books_in_pack

    def test_move_from_school_to_basket(self):
        """Adds school book to the cart"""
        basket_before = check_basket(pytest.web_driver)
        element_click_by_xpath('//li[@data-event-content="Школа"]')
        element_click_by_xpath('//li/label[@class="checkbox-ui label kls kls-3"]')
        element_click_by_xpath('//div[@class="adv-act"]/span[@class ="act-reset"]')
        element_click_by_xpath('//li/label[@class="checkbox-ui label kls kls-4"]')
        element_click_by_xpath('//div[@class="adv-act"]/span[@class="act-close ml10"]')
        element_click_by_xpath('//div[@class="inputs predmet-list"]/div/div/label')
        element_click_by_xpath('//div[@class="qtip-act"]/a')
        element = pytest.web_driver.find_element_by_xpath(
            '//div[@class="products-row "]/div[3]/div/div/div/div[@class="product-buy buy-avaliable fleft"]')
        element.click()
        time.sleep(1)
        element.click()
        time.sleep(2)
        element = pytest.web_driver.find_element_by_xpath('//a[@href="#step1-default"]')
        # print(element.text)
        basket_after = check_basket(pytest.web_driver)
        my_counter = 0
        try:
            for s in element.text.split():
                if s.isdigit():
                    my_counter = int(s)
            print('There are ', my_counter, ' items in my shopping cart')
            assert basket_after == my_counter
        except NoSuchElementException:
            print('\nBasket is empty')
        # check if item is added
        assert (basket_after - basket_before) == 1

    def test_empty_basket(self):
        """Empty the cart"""
        basket_before = check_basket(pytest.web_driver)
        if basket_before == 0:
            print("Cart is empty")
            element_click_by_xpath('//a[@href="/books/"]')
            element_click_by_xpath('//a[@href="/genres/1850/"]')
            element = pytest.web_driver.find_elements_by_xpath(
                '//div[@class ="card-column card-column_gutter col-xs-3 col-sm-2"]')[0]
            element.click()
            element = pytest.web_driver.find_element_by_xpath(
                '//a[@class="btn btn-small btn-primary btn-buy"]')
            element.click()
            time.sleep(2)
        element_click_by_xpath('//li[@class="b-header-b-personal-e-list-item have-dropdown  last-child"]/a')
        element_click_by_xpath('//div[@class="text-regular empty-basket-link"]')
        time.sleep(2)
        element_click_by_xpath('//a[@class="b-link-popup g-alttext-deepblue"]')
        time.sleep(2)
        element_click_by_xpath('//div[@class="text-regular empty-basket-link"]')
        basket_after = check_basket(pytest.web_driver)
        assert basket_after == 0


class TestPutAside:  # testing favorite function, please run entire class for proper work
    def test_move_to_putaside(self):
        """Adds favorite items for later review"""
        hover_move_click(pytest.web_driver, '//a[@href="/games/"]', 10, 80)
        time.sleep(1)
        hover_move_click(pytest.web_driver, 'None', 220, 0)
        time.sleep(2)
        hover_move_click(pytest.web_driver, '//div[@class ="desktop-subnavigagions-block '
                                            'only_desc"]/div/div/div/span[@class="navisort-part navisort-filter '
                                            'navisort-part-2 fleft"]')
        ActionChains(pytest.web_driver).send_keys(Keys.PAGE_DOWN).perform()
        # hover_move_click(pytest.web_driver, '//input[@name="price_min"]')
        element = pytest.web_driver.find_element_by_xpath('//input[@name="price_min"]')
        element.send_keys("1200")
        element = pytest.web_driver.find_element_by_xpath('//input[@name="price_max"]')
        element.send_keys("2400")
        hover_move_click(pytest.web_driver, '//ul[@class="menu-items-list"]/li/label[contains(text(),"Со скидкой")]')
        hover_move_click(pytest.web_driver, 'None', 0, 110)
        time.sleep(5)
        element_click_by_xpath('//*[@id="catalog"]/div/div[3]/div/div[4]/div/div[1]/div/div[3]/div/div[2]/div/div/a['
                               '1]/span')
        element_click_by_xpath('//*[@id="catalog"]/div/div[3]/div/div[4]/div/div[2]/div/div[3]/div/div[2]/div/div/a['
                               '1]/span')
        # check if item is added
        assert pytest.web_driver.find_element_by_xpath('//*[@id="minwidth"]/div[1]/div/div[1]').is_displayed()
        title1 = pytest.web_driver.find_element_by_xpath(
            '//*[@id="catalog"]/div/div[3]/div/div[4]/div/div[1]/div/div[1]/a').get_attribute('title')
        print('\nadded new:\t', title1)
        # # Go up:
        pytest.web_driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
        element = pytest.web_driver.find_element_by_xpath('//a/span[@class="b-header-b-personal-e-icon-wrapper '
                                                          '<!--b-header-b-personal-e-icon-wrapper-m-putorder'
                                                          '-->"]/span[1]/span[2]')
        put_aside_after = element.text
        print('number of items:\t', put_aside_after)
        element_click_by_xpath('//span[@class="b-header-b-personal-e-icon-wrapper '
                               '<!--b-header-b-personal-e-icon-wrapper-m-putorder-->"]')
        elements = pytest.web_driver.find_elements_by_xpath('//div[@class="products-row "]/div[@class="product '
                                                            'need-watch product_labeled product-cart watched"]')
        check_title = 0
        for element in elements:
            title_text = element.get_attribute('data-name')
            print(title_text)
            if title1 == title_text:
                check_title = 1
        # check if item is present
        assert check_title == 1

    def test_putaside_to_delete(self):
        """Checking the favorite items and mark them for deletion.
        The pop-up confirmation window should appear
        However, it is not possible to act on it by the code
        This test shall be run if any item is present, thus, run the entire CLASS to see the proper work"""
        element_click_by_xpath('//span[@class="b-header-b-personal-e-icon-wrapper '
                               '<!--b-header-b-personal-e-icon-wrapper-m-putorder-->"]')
        element_click_by_xpath('//a[@onclick="selectAllPutOrderNew(); return false;"]')
        pytest.web_driver.save_screenshot('mark_all.png')  # screenshot marked items to delete
        time.sleep(2)
        element_click_by_xpath('//*[@id="right-inner"]/div[3]/div/div/a[1]')
        pytest.web_driver.save_screenshot('unmark.png')  # srceenshot unmarked items
        element_click_by_xpath('//a[@onclick="selectAllPutOrderNew(); return false;"]')
        # element_click_by_xpath('//a[@title="Удалить все отложенные товары"]') # this one opens new js pop-up window
        # on which could not operate
