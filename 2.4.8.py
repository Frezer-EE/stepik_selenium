from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
browser.get(link)

WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '10000 RUR'))

browser.find_element_by_id('book').click()

number = int(browser.find_element_by_id('input_value').text)
result = str(math.log(abs(12*math.sin(number))))
input1 = browser.find_element_by_id('answer')
input1.send_keys(result)

browser.find_element_by_id('solve').click()