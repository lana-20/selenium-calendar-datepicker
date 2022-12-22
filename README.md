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
