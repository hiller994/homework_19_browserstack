import os
from pathlib import Path
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from pydantic import BaseModel, Field

import utils.file


class Settings(BaseModel):
    environment: str = Field(..., min_length=1)
    platformName: str = Field(default="android")
    userName: str = Field(default="")
    accessKey: str = Field(default="")
    app: str = Field(..., min_length=1)
    remote_url: str = Field(..., min_length=1)
    deviceName: str = Field(..., min_length=1)
    platformVersion: str = Field(default="")


def load_config() -> Settings:
    #.env с кредами от bstack
    base_env_path = Path('.') / '.env'
    if base_env_path.exists():
        load_dotenv(base_env_path)

    environment = os.getenv('environment')
    if not environment:
        raise ValueError("Не выбрано окружение(environment): bstack или emulator")

    # Выбираем нужный .env файл, в зависимовсти от окружения
    env_path = None
    if environment == 'bstack':
        env_path = Path('.') / '.env.bstack'
    elif environment == 'emulator':
        env_path = Path('.') / '.env.local_emulator'
    elif environment == 'device':
        env_path = Path('.') / '.env.local_real'

    if env_path and env_path.exists():
        load_dotenv(env_path)

    # Обработка пути к приложению
    app_path = os.getenv('app')
    if environment in ('emulator', 'device'):
        if not app_path or app_path.startswith(('http://', 'https://', 'bs://')):
            app_path = str(utils.file.abs_path_from_project('app-alpha-universal-release.apk'))

    return Settings(
        environment=environment,
        platformName=os.getenv('platformName', 'android'),
        userName=os.getenv('BROWSERSTACK_USERNAME', ''),
        accessKey=os.getenv('BROWSERSTACK_ACCESSKEY', ''),
        app=app_path,
        remote_url=os.getenv('remote_url', ''),
        deviceName=os.getenv('deviceName', ''),
        platformVersion=os.getenv('platformVersion', '')
    )

def get_options(settings: Settings):
    options = {
        'platformName': settings.platformName,
        'deviceName': settings.deviceName,
        'app': settings.app,
        'appWaitActivity': "org.wikipedia.*"
    }

    if settings.platformVersion:
        options['platformVersion'] = settings.platformVersion

    if settings.environment == 'bstack':
        options['bstack:options'] = {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": settings.userName,
            "accessKey": settings.accessKey
        }

    return UiAutomator2Options().load_capabilities(options)