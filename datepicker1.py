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

...

driver.close()
