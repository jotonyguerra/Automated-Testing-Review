from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com')
    #driver.find_element(By.LINK_TEXT, 'Form Authentication')
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')
    ))
    wait.until(EC.url_to_be('https://the-internet.herokuapp.com/'))

    
finally:
    driver.quit()
