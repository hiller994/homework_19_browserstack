import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os

from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({"""Это driver options"""
                                                       # Specify device and os_version for testing
                                                       "platformName": "android",
                                                       "platformVersion": "9.0",
                                                       "deviceName": "Google Pixel 3",

                                                       # Set URL of the application under test
                                                       "app": "bs://sample.app",

                                                       # Set other BrowserStack capabilities
                                                       'bstack:options': {
                                                           "projectName": "First Python project",
                                                           "buildName": "browserstack-build-1",
                                                           "sessionName": "BStack first_test",

                                                           # Set your access credentials
                                                           # со страницы https://app-automate.browserstack.com/dashboard/v2/quick-start/get-started
                                                           "userName": "bsuser_siHW2q",
                                                           "accessKey": "w9gfPWcizNSEgHCSGyqT"
                                                       }
                                                       })

    #передаем селениуму драйвер
    #browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.driver_remote_url = "http://hub.browserstack.com/wd/hub"
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    '''
    #BASE_URL тут нет (в мобилке)
    browser.config.base_url = os.getenv(
        'base_url', 'https://www.wikipedia.org'
    )

    #CONFIG DRIVER NAME не нужен
    browser.config.driver_name = os.getenv('driver_name', 'chrome')
    '''

    '''
    #тоже не нужно
    """Запуск драйвера в невидимом режиме"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    browser.config.driver_options = chrome_options
    '''

    '''
    browser.config.hold_driver_at_exit = (
        os.getenv('hold_driver_at_exit', 'false').lower() == 'true'
    )
    '''

    '''
    #НЕ НУЖНО, т.к. разрешение определяется устройством
    browser.config.window_width = os.getenv('window_width', '1024')
    browser.config.window_height = os.getenv('window_height', '768')
    '''


    yield

    browser.quit()
