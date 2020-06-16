import pytest
from selenium import webdriver 

@pytest.fixture
def hello(): 
    return "Hello World"

@pytest.yield_fixture(scope='session')
def driver():
    with webdriver.Remote(command_executor="http://127.0.0.1:9515") as driver:
        yield driver 


def test_hello(hello, driver): 
    driver.get("http://127.0.0.1:8000")
    assert hello in driver.page_source 
    


def test_say_bye(driver): 
    driver.get("http://127.0.0.1:8000/bye")
    assert "bye" in driver.page_source

def test_counter(driver):
    driver.get("http://127.0.0.1:8000/counter")
    element = driver.find_element_by_id("counter")
    assert "1" == element.text
    driver.refresh()
    element = driver.find_element_by_id("counter")
    assert "2" == element.text
