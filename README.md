# Calendar Element Date Picker

There are 2 kinds of elements I typically encounter on a web page:
1. Standard
2. Non-standard / Customized

Standard elements, such as buttons, checkboxes, links, images, etc., are the same everywhere. Non-standard elements differ from each other, their design varies among apps. Eg, I take a date picker in one app, it differs from the date picker in another app. The reason to call a non-standard element 'customized' is because it contains multiple standard elements. A date picker itself is a combination of multiple web elements, which contains
a dropdown or dates arranged in a table, sometimes I see arrow marks, buttons, etc. So, a date picker is a customized element, which is designed using standard elements. That is why I do not see the same date picker on every web page and my automation script cannot be reused. I write automation code in accordance with each date picker design.

This tutorial covers 2 types of date pickers.

First, let's try https://jqueryui.com/datepicker/.

<img src="https://user-images.githubusercontent.com/70295997/209210369-49735f12-6524-4621-9b4a-6afc57c25973.png" width=400>

It contains a simple input box. I can identify the element and use the _.send_keys()_ method to pass the date. This works 90% of the time. But some apps, like CRM, do not allow me to use this method. I cannot pass the value or type anything. In those cases, I have to select the date through the date picker.

To open the date picker, perform the click action inside the input box. From the picker, I should be able to select the year, month and date.

Identify the element, it's inside a frame. I need to switch to the frame with the _.switch_to()_ command before I can interact with the element. Inside this page there's only one frame, so I use an index of tbe frame (instead of name or id). Only when I have one frame on the page, I can directly pass the index of zero.

        driver.switch_to.frame(0)

<img src="https://user-images.githubusercontent.com/70295997/209210572-fdd745ad-7619-4037-b855-0cc0cb121739.png" width=600>

The input box accepts a date in the MM/DD/YYYY format.

<img src="https://user-images.githubusercontent.com/70295997/209222859-131a02ff-6a02-4b98-a176-cc75ebfe220e.png" width=600>)

        driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("12/22/2022")		# MM/DD/YYYY

This is a straightforward approach, where I need only send the keys. Sometimes it's not allowed, then I have to write the logic to select the date.

Define 3 variables for the date input:

        year="2023"
        month="January"
        date="23"

        driver.find_element(By.XPATH, "//input[@id='datepicker']").click()	# open datepicker

Initially, I focus on the month and year. The current month and year display as soon I open the datepicker. I need to capture those 2 elements (month and year) separately and compare them to my expected ones. If they match, immediately proceed inside the table with dates and select the desired date.

If the actual month and year do not match the expected ones, then I click on the Next arrow mark to get the following month and year. Again, capture the actual values and compare to the expected ones. If they aren't equal, click on the Next arrow mark again and repeat the comparison steps. I click on Next n-number of times until I get the month and year, which match the expected values defined in the script. So, I have to be clicking the arrow mark as many times as it takes to reach my expected month and year. Only then I can stop. But I don't know exactly when that happens, that's why I don't know exactly how many times I have to click.

When not knowing the end/stop condition, I use the while-loop. When I know the start and end point, then I use the for-loop. Here, I don't know how many times to click the arrow mark, i.e. don't know the condition. For that reason, I use the while-loop. Inside the loop, I capture the month and year.

![image](https://user-images.githubusercontent.com/70295997/209240690-6104cce0-20e8-43ca-9c05-9c19af2436f9.png)

        # Select month and year
        while True:	
                mo = driver.find_element(By, XPATH, "//span[@class='ui-datepicker-month']").text
                yr = driver.find_element(By, XPATH, "//span[@class='ui-datepicker-year']").text

                if mo == month and yr == year:		
                        break
                else:
                        driver.find_element(By. XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()	# Next arrow

Once the correct month and year are selected, I proceed to handle the date. The date selection table changes, depending on the month and year. I need to get all the dates from the table as a list.

<img src="https://user-images.githubusercontent.com/70295997/209242924-165a2cc1-c805-43d6-be3c-3761df70624c.png" width=600>)

I don't need all the contents of the table tag. Only a specific date from 1 to 28, 29, 30 or 31. First, I capture all the dates from the datepicker, then read them one by one, until I reach the expected date. A looping statement is required. I write an Xpath to point to all the anchor tags inside the _td_'s, inside the _tr_ tags if the _tbody_.

        //table[@class='ui-datepicker-calendar']/tbody/tr/td/a

![image](https://user-images.githubusercontent.com/70295997/209251165-d4854b5e-2511-4ed4-8c0f-f6abcee79750.png)

Tomorrow, even if I change month and year, this Xpath will still point to all the dates.

![image](https://user-images.githubusercontent.com/70295997/209251798-4ed8d920-41eb-475e-beb6-51cb3e4fa83a.png)

Use this Xpath to capture all the date elements from the table.

dates = driver.find_element(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

From all the dates, I need to choose one date. To find that, I write a for-loop statement. As soon as the text value of a date matches my expected date condition, I click on it. Upon clicking on the desired element, I break out of the loop, because there's no need to keep interating through the remainder of the _dates_ multiple times.

for dt in dates:
	if dt.text == date:
		dt.click()
		break

This is the logic to select the date, when I cannot directly type (send keys) the date into the input box. It works for selecting a current or future date. 

But what if I want to select a date from the past? I repeat the same logic. Except that instead of clicing on the Next arow mark, I click on the Prev arrow. I have to go in the rightward direction.

Identify the Xpath locator for the Prev arrow mark and test an old date from the past. I cannot use both (future and past) dates at the same time, only one.

        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click	# Prev arrow

        # past date test data
        year="2021"
        month="August"
        date="12"

Usually there are 2 scenarios when working with a datepicker, and only 1 option is enabled in the app:
1) travel apps - take a current or future date for departures and returns, because there is no travel in the past
2) DOB pickers - take a past date, because the date of birth cannot occur in the future

While a demo app allows both the selection of a date in the future or in the past, a production app goes only in either one of those directions. But even in a demo app, I cannot select both dates concurrently, only select one option at a time.

So, this is how I commonly implement the logic for the datepicker test cases. 

Some datepickers are easy - can directly select the month and year from a dropdown. Let's explore this example with https://www.dummyticket.com/dummy-ticket-for-visa-application/.





