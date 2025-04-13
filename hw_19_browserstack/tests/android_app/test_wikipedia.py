from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as have
from selene import have,be, browser
import time


def test_search():
    '''
    search_element = WebDriverWait(driver, 30).until(
        have.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
    )
    search_element.click()
    '''
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    '''
    search_input = WebDriverWait(driver, 30).until(
        have.element_to_be_clickable(
            (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
    )
    search_input.send_keys("BrowserStack")
    '''
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Appium")

    #time.sleep(5)
    '''
    search_results = driver.find_elements(AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
    '''
    results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
    #assert (len(results) > 0)
    results.should(have.size_greater_than(0)) #проверяем, что кол-во результатов больше 0, наверное результатов после ввода в поиск
    #results.first.should(have.text('Appium')) первый результат в поиске Appium