from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://0.0.0.0:8080/new_project")
pid = driver.find_element_by_name('pid')
username = driver.find_element_by_name('username')
title = driver.find_element_by_name('title')
confirm = driver.find_element_by_id('confirm')
pid.send_keys("some text")
username.send_keys("some text")
title.send_keys("some text")
confirm.send_keys(Keys.ENTER)
assert driver.page_source.find("Project ID")
driver.close()
