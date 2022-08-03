from appium import webdriver
from os import path 

#installing appium, and ios compatible software

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.app.zip')
APPIUM = 'https://localhost:4723' #change port

CAPS = {
    'platformName': 'iOS',
    'platformVersion': '13.6', #may need to change
    'deviceName': 'iPhone 11',
    'automationName': 'XCUITest',
    'app': APP 
}


driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)
driver.quit()
