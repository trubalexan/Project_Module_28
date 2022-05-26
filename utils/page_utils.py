import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains


def open_page(web_browser, url: str, scroll: str = 'up'):
    """ This is advanced function which also checks that all images completely loaded. """

    web_browser.get(url)

    page_loaded = False
    images_loaded = False

    script = ("return arguments[0].complete && typeof arguments[0].natural"
              "Width != \"undefined\" && arguments[0].naturalWidth > 0")

    # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
    while not page_loaded and not images_loaded:
        time.sleep(1)

        # Scroll down and wait when page will be loaded:
        web_browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        page_loaded = web_browser.execute_script("return document.readyState == 'complete';")

        # Make sure that every image loaded completely
        # (sometimes we have to scroll to the image to push browser upload it):
        pictures = web_browser.find_elements_by_xpath('//img')
        res = []

        for image in pictures:
            src = image.get_attribute('src')
            if src:
                # Scroll down to each image on the page:
                image.location_once_scrolled_into_view
                web_browser.execute_script("window.scrollTo(0, 155)")

                image_ready = web_browser.execute_script(script, image)

                if not image_ready:
                    # if the image not ready, give it a try to load and check again:
                    time.sleep(5)
                    image_ready = web_browser.execute_script(script, image)

                res.append(image_ready)

        # Check that every image loaded and has some width > 0:
        images_loaded = False not in res

    if scroll == 'up':
        # Go up:
        web_browser.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
    elif scroll == 'down':
        # Go down:
        web_browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    else:
        pass
    # # Go up:
    # web_browser.execute_script('window.scrollTo(document.body.scrollHeight, 0);')

    # # Go down:
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def scroll_to_bottom(driver):
    """Scrolls web page to the bottom"""
    old_position = 0
    new_position = None

    while new_position != old_position:
        # Get old scroll position
        old_position = driver.execute_script(
            ("return (window.pageYOffset !== undefined) ?"
             " window.pageYOffset : (document.documentElement ||"
             " document.body.parentNode || document.body);"))
        # Sleep and Scroll
        time.sleep(1)
        driver.execute_script((
            "var scrollingElement = (document.scrollingElement ||"
            " document.body);scrollingElement.scrollTop ="
            " scrollingElement.scrollHeight;"))
        # Get new position
        new_position = driver.execute_script(
            ("return (window.pageYOffset !== undefined) ?"
             " window.pageYOffset : (document.documentElement ||"
             " document.body.parentNode || document.body);"))


def hover_simple(web_browser, locator):
    """Making mouseover on given locator"""
    element = web_browser.find_element_by_xpath(locator)
    hov = ActionChains(web_browser).move_to_element(element)
    hov.perform()


def hover_move_click(web_browser, locator: str, x: int = 0, y: int = 0):
    """Making mouseover on given locator, then move cursor and click
    If locator is 'None', performing just move cursor and click"""
    if locator == 'None':
        ActionChains(web_browser).move_by_offset(x, y).click().perform()
    else:
        element = web_browser.find_element_by_xpath(locator)
        hov = ActionChains(web_browser).move_to_element(element)
        hov.perform()
        ActionChains(web_browser).move_by_offset(x, y).click().perform()


def hover(web_browser, locator: str, x: int, y: int, link: str):
    """Making mouseover on given locator, then move cursor and click other link element"""
    element = web_browser.find_element_by_xpath(locator)
    hov = ActionChains(web_browser).move_to_element(element)
    hov.perform()
    ActionChains(web_browser).move_by_offset(x, y).perform()
    element = web_browser.find_element_by_xpath(link)
    hov_link = ActionChains(web_browser).move_to_element(element)
    hov_link.click().perform()


def check_basket(web_browser):
    """This method is checking the basket items counter and returns it as an integer"""
    basket_items = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')
    counter = basket_items.text
    print('\nItems in basket:\t', counter)
    return int(counter)


def element_click_by_xpath(locator: str):
    """Performing a click on given locator"""
    element = pytest.web_driver.find_element_by_xpath(locator)
    element.click()
    time.sleep(2)
