import allure
import pytest
from selene import browser
from appium import webdriver

import config
import utils
from config import load_config, get_options
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    settings = load_config()
    attach.view_environment() # ДЛЯ АЛЛЮРА
    options = get_options(settings)

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            settings.remote_url,
            options=options
        )

    browser.config.timeout = 10.0

    yield

    attach.screenshot()
    attach.page_source_xml()

    session_id = browser.driver.session_id
    with allure.step('tear down app session'):
        browser.quit()
    if settings.environment == 'bstack':
        attach.bstack_video(session_id)