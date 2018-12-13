from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://0.0.0.0:8080")
assert "Project Viewer" in driver.title
driver.close()
