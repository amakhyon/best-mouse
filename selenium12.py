import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  

driver = webdriver.Chrome()

driver.get("https://amazon.com")

search = driver.find_element_by_id("twotabsearchtextbox")


search.send_keys("gaming mouse")
search.send_keys(Keys.RETURN)
time.sleep(1)

mouses = driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")

prices = driver.find_elements_by_xpath("//span[@class='a-price-whole']")

prices_text = []
for price in prices: #to remove the XX. that ruins the string to int conversion
	pricy = price.text
	pricy.replace('.', '')
	prices_text.append(pricy)
	print(pricy)
prices_int = []

try:
	next_button = driver.find_element_by_xpath("//*[contains(text(), 'Next Page')]")
except:
	next_button = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")


next_button.click()