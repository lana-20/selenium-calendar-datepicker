from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)	  # switch to frame
datepicker = driver.find_element(By.XPATH, "//input[@id='datepicker']")

datepicker.send_keys("12/22/2022")		# MM/DD/YYYY

#----Select/test one date at a time - past or future - not both----#
# future date test data
year="2023"
month="January"
date="23"

# past date test data
# year="2021"
# month="August"
# date="12"

datepicker.click()	# open datepicker

# Select month and year
while True:	
	mo = driver.find_element(By, XPATH, "//span[@class='ui-datepicker-month']").text
	yr = driver.find_element(By, XPATH, "//span[@class='ui-datepicker-year']").text

	if mo == month and yr == year:		
		break
	else:
		driver.find_element(By. XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()	# Next arrow
#  		driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click	# Prev arrow

# Select date
dates = driver.find_element(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for dt in dates:
	if dt.text == date:
		dt.click()
		break

driver.close()
