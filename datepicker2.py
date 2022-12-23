from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

...

driver.close()
