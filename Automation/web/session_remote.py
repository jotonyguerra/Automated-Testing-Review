from selenium import webdriver

caps = {
    'browserName': 'chrome'
}
driver_location = r'C:\Users\joton\OneDrive\Documents\Projects\Web Testing Automation\web\chromedriver_win32\chromedriver.exe'

driver = webdriver.Remote(
    command_executor='https://localhost:4444',
    desired_capabilities=caps
)


driver.quit()
