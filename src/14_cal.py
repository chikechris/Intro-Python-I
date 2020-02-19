"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html
Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# QUESTIONS:
    # 1. Do we use sys to grab current month from system? Why is this imported?
      # so we can add the arguments from the user and do something with them like in the modules.py
    # 2. How do to use calender?
    # 3. How to use datetime?

# Need conditional statement:
    # 1 - No user input --> output current date (datetime)
    # 2 - If user specifies one input --> assume month input and output month of current year
    # 3 - If user put in both inputs --> assume both inputs and output month and year of inputs
    # 4 - Incorrect --> output expected inputs to be given by user 
    # exit program

# user input
args = sys.argv

"""
|---- 0 ----|--- 1 ---|-- 2 -- |
['14_cal.py', 'month',  'year']
"""
# print(len(args)) # Prints length of 3 

current_month = int(datetime.now().month)
current_year = int(datetime.now().year)

# no inputs --> current datetime 
if len(args) == 1:
    print(calendar.month(current_year, current_month))
    # print("There are no arguments")

# month input --> current year datetime
elif len(args) == 2:
    month = int(args[1]) 
    print(args[1])
    print(calendar.month(current_year , month) )
    # print("There is a month but no year")

# month & year input --> user inputs
elif len(args) == 3:
    month = int(args[1]) 
    year = int(args[2])
    print(calendar.month(year, month))
    # print("Month and a Year")

#invalid input --> more than just month and year
else:
    print("Month has to be formatted as a whole number (1 - 12); Years must be 4 digits (eg, 2018)")



print(args)
