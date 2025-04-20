import pytest
from appium.options.ios import XCUITestOptions
from selene import browser
import os

from draft.config0 import settings
from draft.draft2.utils import attach


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = XCUITestOptions().load_capabilities({"""Это driver options"""
                                                       # Specify device and os_version for testing
                                                       "platformName": "ios",
                                                       "platformVersion": "16",
                                                       "deviceName": "iPhone 14 Pro Max",

                                                       # Set URL of the application under test
                                                       "app": "bs://sample.app",

                                                       # Set other BrowserStack capabilities
                                                       'bstack:options': {
                                                           "projectName": "First Python project",
                                                           "buildName": "browserstack-build-ios",
                                                           "sessionName": "BStack first_test",

                                                           # Set your access credentials
                                                           # со страницы https://app-automate.browserstack.com/dashboard/v2/quick-start/get-started
                                                           "userName": settings.BROWSERSTACK_USERNAME,
                                                           "accessKey": settings.BROWSERSTACK_ACCESSKEY
                                                       }
                                                       })

    #передаем селениуму драйвер
    #browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.driver_remote_url = "http://hub.browserstack.com/wd/hub"
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    
    yield

    attach.add_logs(browser)
    attach.add_screenshot(browser)

    browser.quit()
