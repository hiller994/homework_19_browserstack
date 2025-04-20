import os

from pydantic_settings import BaseSettings

#run_on_bstack = os.getenv('run_on_bstack', 'false').lower() == 'true' # false - не запускать по умолчанию run_on_bstack и сравниваю с true (boolen), чтобы получить тру или фолс
remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723')
deviceName = os.getenv('deviceName') #если названия устройства не будет, то None
appWaitActivity = os.getenv('appWaitActivity', "org.wikipedia.*")
app = os.getenv('app', '../app-alpha-universal-release.apk')
runs_on_bstack = app.startswith('bs://')
if runs_on_bstack:
    remote_url = 'https://hub.browserstack.com/wd/hub'

'''
def runs_on_bstack():
    return app.startswith('bs://')
'''


class Config(BaseSettings):
    BROWSERSTACK_USERNAME: str
    BROWSERSTACK_ACCESSKEY: str

settings1 = Config(_env_file="draft2/.env")

print(settings1.BROWSERSTACK_USERNAME)
print(settings1.BROWSERSTACK_ACCESSKEY)
'''

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BROWSERSTACK_USERNAME: str
    BROWSERSTACK_ACCESSKEY: str

    class Config:
        env_file = ".env"

creds = Settings()
print(creds.BROWSERSTACK_USERNAME)
print(creds.BROWSERSTACK_ACCESSKEY)
'''
