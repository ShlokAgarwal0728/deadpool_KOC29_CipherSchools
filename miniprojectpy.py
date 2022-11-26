# Python program to calculate how many days person survived in this world

from datetime import date

day1  = date.today()             #CURRENT DATE
day2 = date(2005, 1, 5)          #BIRTH DATE (yyyy,mm,dd)
diff = day1 - day2
print(diff.days)
