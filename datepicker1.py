from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)	  # switch to frame
datepicker = driver.find_element(By.XPATH, "//input[@id='datepicker']")

datepicker.send_keys("12/22/2022")		# MM/DD/YYYY

year="2023"
month="January"
date="23"

datepicker.click()	# open datepicker

# Select month and year
while True:	
	mo = driver.find_element(By, XPATH, "//span[@class='ui-datepicker-month']").text
	yr = driver.find_element(By, XPATH, "//span[@class='ui-datepicker-year']").text

	if mo == month and yr == year:		
		break
	else:
		driver.find_element(By. XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()	# Next arrow

# Select date    

...

driver.close()
