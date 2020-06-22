import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def hello():
    return "Hello World"


@pytest.yield_fixture(scope='session')
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    with webdriver.Chrome(chrome_options=chrome_options) as driver:
        yield driver


def test_hello(hello, driver, live_server):
    driver.get(live_server.url)
    assert hello in driver.page_source


def test_say_bye(driver, live_server):
    driver.get(live_server.url + "/bye")
    assert "bye" in driver.page_source


def test_counter(driver, live_server):
    driver.get(live_server.url + "/counter")
    element = driver.find_element_by_id("counter")
    assert "1" == element.text
    driver.refresh()
    element = driver.find_element_by_id("counter")
    assert "2" == element.text
