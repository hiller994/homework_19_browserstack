import allure
from selene import browser
import requests

from config import load_config
settings = load_config()

def screenshot():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name = 'screenshot',
        attachment_type = allure.attachment_type.PNG,
    )


def page_source_xml():
    allure.attach(
        browser.driver.page_source,
        name = 'screen xml dump',
        attachment_type = allure.attachment_type.XML,
    )


def bstack_video(session_id):
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth = (settings.userName, settings.accessKey),
    ).json()
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name = 'video recording',
        attachment_type = allure.attachment_type.HTML,
    )

def view_environment():
    # для передачи environment в отчет аллюр
    allure.dynamic.parameter("Environment", settings.environment)