import datetime

# # Input
# input_date = input("Input a date as yyyy,mm,dd: ") #This method failed to parse days separated by comma.

# # First working Input Method
# input_year = int(input("Enter a year: ")) #int(2022) #Needed to import as separate days. Could not interpret 2022, 3, 3 as 3 separrate integers.
# input_month = int(input("Enter a month: ")) #int(3)
# input_day = int(input("Enter a day: ")) #int(3)
# day = datetime.date(input_year, input_month, input_day) #Uses weekday function to determine weekday

# # Second Input Method. Clever parsing from StackOverflow
input_date = input("Input a date as yyyy,mm,dd: ")
input_year, input_month, input_day = (int(x) for x in input_date.split(','))
day = datetime.date(input_year, input_month, input_day)

print()

# # First Method
# weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# weekday = weekdays[day.weekday()] #First method I used

# # Second Method
# weekdays[day.weekday()]datetime.today().strftime('%A') #Code from StackOverflow.
# strftime converts to readable datetime format.
weekday = day.strftime('%A') #This format doesn't require a list of weekdays.

# Third Method
# import calendar
# my_date = date.today()
# calendar.day_name[my_date.weekday()]

print("On " + str(day) + " the day of the week is " + weekday)