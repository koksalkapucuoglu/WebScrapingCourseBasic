from selenium import webdriver
import time

browser = webdriver.Chrome('chromedriver')

browser.get('https://www.forbes.com/powerful-brands/list/1')

browser.page_source #get source code for page 

browser.title #get page title

browser.fullscreen_window()
time.sleep(1)
browser.get('https://www.forbes.com/companies/apple/?list=powerful-brands')
browser.set_window_size(800,600)
browser.save_screenshot('image.png')
time.sleep(3)
browser.back()
time.sleep(1)
browser.quit()