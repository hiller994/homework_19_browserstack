import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os

from draft.draft2.utils.attach import attach_screenshot


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    # Получаем абсолютный путь к APK
    current_dir = os.path.dirname(os.path.abspath(__file__))
    apk_path = os.path.abspath(os.path.join(
        current_dir,
        "../../../hw_19_browserstack/tests/test_app_local/app-alpha-universal-release.apk"
    ))

    # Проверяем существование файла
    if not os.path.exists(apk_path):
        pytest.fail(f"APK file not found at: {apk_path}")

    options = UiAutomator2Options().load_capabilities({
        #"appium:app": apk_path,
        #"appium:appWaitActivity": "org.wikipedia.*",
        #"appium:udid": "2e9b4f69",
        #"appium:noReset": True

        #"platformName": "Android",
        #"appium:automationName": "UiAutomator2",
        "appium:app": apk_path,
        "appium:appWaitActivity": "org.wikipedia.*",
        "appium:allowTestPackages": True, #Разрешает установку тестовых пакетов (например, приложений с отладочной подписью).
        "appium:udid": "emulator-5554", #2e9b4f69 - реальное устройство, emulator-5554 - эмулятор
        "appium:ignoreHiddenApiPolicyError": True, #Игнорирует ошибки доступа к скрытым API в Android (актуально для Android 9+).
        #"appium:enforceAppInstall": False, #Не принуждает переустановку приложения при каждой сессии.
        #"appium:relaxedSecurity": True, #Ослабляет некоторые проверки безопасности в Appium для упрощения тестирования.
        #"appium:noRestrictPermissions": True, #Не ограничивает разрешения при установке приложения.
        #"appium:dontStopAppOnReset": True, #Не останавливает приложение при сбросе состояния.
        #"appium:noReset": True, #Не сбрасывает состояние приложения между сессиями (сохраняет данные).
        #"appium:fullReset": False #Полностью отключает сброс приложения и очистку данных (включая удаление приложения после тестов).
    })

    #browser.config.driver = webdriver.Remote(
    #    command_executor='http://127.0.0.1:4723',
    #   options=options
    browser.config.driver_remote_url = "http://127.0.0.1:4723"
    browser.config.driver_options = options



    yield

    attach_screenshot(browser)
    browser.quit()


