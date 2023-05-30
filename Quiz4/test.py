from selenium import webdriver
import time
path = '/Users/NikaGamkrelidze/Downloads/chromedriver_mac64_(1)/chromedriver'

driver = webdriver.Chrome(path)

driver.get('https://tkt.ge/')

id = "desktop-search-input"



time.sleep(10000)