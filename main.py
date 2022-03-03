import datetime
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# input_date = input("Input a date as yyyy,mm,dd: ")
input_year = int(2022) #Needed to import as separate days. Could not interpret 2022, 3, 3 as 3 separrate integers.
input_month = int(3)
input_day = int(3)

day = datetime.date(input_year, input_month, input_day)

print("On " + str(day) + " the day of the week is " + weekdays[day.weekday()])