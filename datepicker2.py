from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# Date of birth
driver.find_element(By.XPATH, "//input[@id='dob']").click()	# opens datepicker

datepicker_month = Select(driver.find_element(By.XPATH, "//*[@class='ui-datepicker-month']"))
datepicker_month.select_by_visible_text("Dec")

datepicker_year = Select(driver.find_element(By.XPATH, "//*[@class='ui-datepicker-year']"))
datepicker_year.select_by_visible_text("1990")

...

driver.close()
