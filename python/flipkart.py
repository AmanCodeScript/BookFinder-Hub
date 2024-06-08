from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()

URL = 'https://www.flipkart.com/'

def flipkart(toFind):
    driver.get(URL)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

    # Input book name to find
    xpath = '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input'
    field = driver.find_element(by=By.XPATH, value=xpath)
    field.send_keys(toFind)
    field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

    # Find and analyse results after search 
    className = 'cPHDOP'
    eleList = driver.find_elements(by=By.CLASS_NAME, value=className)
    print(len(eleList))
    # print(eleList)


    input()
    driver.quit()


if __name__ == '__main__':
    flipkart('hands-on python')
