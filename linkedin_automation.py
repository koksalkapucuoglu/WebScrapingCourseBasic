from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome('chromedriver')

browser.get('https://tr.linkedin.com/')
browser.set_window_size(1080,860)
time.sleep(1)

#browser.fullscreen_window()
#time.sleep(2)
login = browser.find_element_by_xpath('/html/body/nav/div/a')
login.click()
time.sleep(2)

email = browser.find_element_by_xpath('//*[@id="username"]')
password = browser.find_element_by_xpath('//*[@id="password"]')

email.send_keys('koksalkapucuoglu@hotmail.com')
password.send_keys('*********')

login_button = browser.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button')
login_button.click()
time.sleep(5) 

search_bar = browser.find_element_by_xpath('//*[@id="ember20"]/input')
search_bar.send_keys('#python')
search_bar.send_keys(Keys.RETURN)
time.sleep(5) 

contacts = browser.find_element_by_xpath('//*[@id="ember26"]/span')
contacts.click()
time.sleep(2) 
contacts_button = browser.find_element_by_xpath('//*[@id="ember1797"]/div/div[1]')
contacts_button.click() 
time.sleep(5) 

for i in range(3):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)') 
    time.sleep(3)

mycontacts = browser.find_elements_by_class_name('mn-connection-card__details')
contact_list = []

for mycontact in mycontacts:
    contact_list.append(mycontact.text)

with open('contact.txt', 'w', encoding='UTF-8') as file:
    for contact in contact_list:
        file.write(contact + '\n')

print('Bağlantılar contact.txt dosyasına yazılıyor...')
time.sleep(5)

browser.quit()