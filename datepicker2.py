from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService	# Selenium 4 https://www.selenium.dev/selenium/docs/api/py/webdriver_chrome/selenium.webdriver.chrome.service.html

# driver = webdriver.Chrome(ChromeDriverManager().install())	# Selenium 3
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))	# Selenium 4

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# Date of birth
driver.find_element(By.XPATH, "//input[@id='dob']").click()	# opens datepicker

datepicker_month = Select(driver.find_element(By.XPATH, "//*[@class='ui-datepicker-month']"))
datepicker_month.select_by_visible_text("Dec")  # month

datepicker_year = Select(driver.find_element(By.XPATH, "//*[@class='ui-datepicker-year']"))
datepicker_year.select_by_visible_text("1990")  # year

all_dates = driver.find_element(BY.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td//a")

for date in all_dates:
  if date.text == "25":
    date.click()
		break

driver.close()
