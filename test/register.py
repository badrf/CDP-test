from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://0.0.0.0:8080/register")
email = driver.find_element_by_name('email')
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
password2 = driver.find_element_by_name('password2')
confirm = driver.find_element_by_id('confirm')
email.send_keys("sometext@test.fr")
username.send_keys("some text")
password.send_keys("some text")
password2.send_keys("some text")
assert driver.page_source.find("Inscription")
driver.close()
