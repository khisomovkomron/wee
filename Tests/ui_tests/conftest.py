import pytest
from loguru import logger
import time
from allure_commons.types import AttachmentType
from traceback import print_stack
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.options import Options
import allure


@pytest.fixture(scope="function", name="user_browser")
def user_browser(request):
    return request.config.getoption("browser")


@pytest.fixture(scope="function", name="browser")
def chrome(user_browser):
    options = Options()
    with allure.step(f'Setting up browser {user_browser}... '):
        pass
    if user_browser.lower() == "edge":
        options = webdriver.EdgeOptions()
        options.set_capability("selenoid:options", {"enableVNC": True})
        browser = webdriver.Remote(command_executor="http://docker-infra.bastion-tech.ru:4444/wd/hub",
                                   options=options)
        browser.maximize_window()
        yield browser
        with allure.step('Shutting down browser... '):
            pass
        browser.quit()
    elif user_browser.lower() == 'local_chrome':
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        browser.maximize_window()
        yield browser
        browser.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", help='Browser to start tests')
    parser.addoption('--stand', help='Stand to start tests')
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="function")
def stand(request):
    return request.config.getoption("stand")


def pytest_collection_modifyitems(items):
    for item in items:
        item.add_marker(pytest.mark.ui)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':

        feature_request = item.funcargs['request']

        driver = feature_request.getfixturevalue('browser')

        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            file_name = str(round(time.time() * 1000))
            allure.attach(driver.get_screenshot_as_png(), name=file_name, attachment_type=AttachmentType.PNG)
        report.extra = extra
