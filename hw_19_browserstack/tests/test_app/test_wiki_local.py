import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_search():
    with allure.step('Пропускаем приветственную страницу'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()
    with allure.step("Кликам по поиску"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    with allure.step("Вводим значение в поиск"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Android")
    with allure.step("Кликаем по результату запроса"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")).click()
    with allure.step("Проверка открытия страницы"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/closeButton")).click() #сначала закрываем всплывашку
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/page_web_view")).should(be.visible)
'''
def test_tab_saved():
    with allure.step('Пропускаем приветственную страницу'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()
    with allure.step("Переходим в раздел 'Saved'"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/nav_tab_reading_lists")).click()
    with allure.step("Проверяем открытие раздела 'Saved'"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/containerClickArea")).should(be.visible)

def test_tab_edits():
    with allure.step('Пропускаем приветственную страницу'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()
    with allure.step("Переходим в раздел 'Edits'"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/nav_tab_edits")).click()
    with allure.step("Проверяем открытие раздела 'Saved'"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/containerClickArea")).should(be.visible)

def test_tab_explore():
    with allure.step('Пропускаем приветственную страницу'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()
    with allure.step("Переходим в раздел 'Explore'"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/nav_tab_explore")).click()
    with allure.step("Проверяем открытие раздела 'Saved'"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_container")).should(be.visible)
'''

