from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from data import MAINPAGE, DRIVER_PATH_CHROME, DRIVER_PATH_FIREFOX, BROWSER
import pytest


# import requests


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(f"\nТест шел: {end_time - start_time}")


@pytest.fixture(scope="session", autouse=True)
def test_driver():
    # получение объекта веб-драйвера для нужного браузера в полноэкранном режиме
    if BROWSER == 'Chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--kiosk')
        pytest.web_driver = webdriver.Chrome(DRIVER_PATH_CHROME, options=chrome_options)
    elif BROWSER == 'Firefox':
        firefox_options: Options = webdriver.FirefoxOptions()
        firefox_options.add_argument('-foreground')
        firefox_options.add_argument('--kiosk')
        # firefox_options.set_preference('browser.anchor_color', '#FF0000')
        pytest.web_driver = webdriver.Firefox(options=firefox_options, executable_path=DRIVER_PATH_FIREFOX)

    pytest.web_driver.get(MAINPAGE)

    pytest.web_driver.find_element_by_xpath(
        '//button[@class="cookie-policy__button js-cookie-policy-agree"]').click()

    yield
    pytest.web_driver.implicitly_wait(1)
    pytest.web_driver.quit()


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     # This function helps to detect that some test failed
#     # and pass this information to teardown:
#
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep
#
#
# def get_test_case_docstring(item):
#     """ This function gets doc string from test case and format it
#         to show this docstring instead of the test case name in reports.
#     """
#
#     full_name = ''
#
#     if item._obj.__doc__:
#         # Remove extra whitespaces from the doc string:
#         name = str(item._obj.__doc__.split('.')[0]).strip()
#         full_name = ' '.join(name.split())
#
#         # Generate the list of parameters for parametrized test cases:
#         if hasattr(item, 'callspec'):
#             params = item.callspec.params
#
#             res_keys = sorted([k for k in params])
#             # Create List based on Dict:
#             res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
#             # Add dict with all parameters to the name of test case:
#             full_name += ' Parameters ' + str(', '.join(res))
#             full_name = full_name.replace(':', '')
#
#     return full_name
#
#
# def pytest_itemcollected(item):
#     """ This function modifies names of test cases "on the fly"
#         during the execution of test cases.
#     """
#
#     if item._obj.__doc__:
#         item._nodeid = get_test_case_docstring(item)
#
#
# def pytest_collection_finish(session):
#     """ This function modified names of test cases "on the fly"
#         when we are using --collect-only parameter for pytest
#         (to get the full list of all existing test cases).
#     """
#
#     if session.config.option.collectonly is True:
#         for item in session.items:
#             # If test case has a doc string we need to modify it's name to
#             # it's doc string to show human-readable reports and to
#             # automatically import test cases to test management system.
#             if item._obj.__doc__:
#                 full_name = get_test_case_docstring(item)
#                 print(full_name)
#
#         pytest.exit('Done!')
