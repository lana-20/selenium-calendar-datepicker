# Calendar Element Date Picker

There are 2 kinds of elements I typically encounter on a web page:
1. Standard
2. Non-standard / Customized

Standard elements, such as buttons, checkboxes, links, images, etc., are the same everywhere. Non-standard elements differ from each other, their design varies among apps. Eg, I take a date picker in one app, it differs from the date picker in another app. The reason to call a non-standard element 'customized' is because it contains multiple standard elements. A date picker itself is a combination of multiple web elements, which contains
a dropdown or dates arranged in a table, sometimes I see arrow marks, buttons, etc. So, a date picker is a customized element, which is designed using standard elements. That is why I do not see the same date picker on every web page and my automation script cannot be reused. I write automation code in accordance with each date picker design.

This tutorial covers 2 types of date pickers.

First, let's try https://jqueryui.com/datepicker/.
