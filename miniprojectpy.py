# Python program to calculate how many days person survived in this world

from datetime import date

day1  = date.today()             #CURRENT DATE
day2 = date(2005, 1, 5)          #BIRTH DATE (yyyy,mm,dd)
diff = day1 - day2
print(diff.days)


# #let's make a program to calculate how much days they lived on earth

# #let's take users date of birth with year and month
# day=int(input("write birth date ="))
# month=int(input("write birth month ="))
# year=int(input("write birth year ="))
#  #let's convert users date of birth in datetime format
# import datetime as dt

# birth=dt.date(year,month,day)
# today=dt.date.today()
# delta=today-birth
# print(delta)
