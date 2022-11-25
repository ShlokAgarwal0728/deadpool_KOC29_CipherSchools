# Python program to calculate how many days person survived in this world

def findAge(current_date, current_month, current_year,
            birth_date, birth_month, birth_year):

    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (birth_date > current_date):
        current_month = current_month - 1
        current_date = current_date + month[birth_month - 1]

    # the difference
    if (birth_month > current_month):
        current_year = current_year - 1;
        current_month = current_month + 12;

    # calculate date, month, year
    calculated_date = current_date - birth_date;
    calculated_month = current_month - birth_month;
    calculated_year = current_year - birth_year;

    # print present age
    print
    "Present Age"
    print("Years:", calculated_year, "Months:",
          calculated_month, "Days:", calculated_date)


#Current dd//mm//yyyy
current_date = int(input("Current Date: "))
current_month = int(input("Current Month: "))
current_year = int(input("Current Year: "))

# birth dd//mm//yyyy
birth_date = int(input("Birth Date: "))
birth_month = int(input("Birth Month: "))
birth_year = int(input("Birth Year: "))

findAge(current_date, current_month, current_year,
        birth_date, birth_month, birth_year)