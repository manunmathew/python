# datetime module
import datetime

#date() convert data into date format


# year=int (input("Enter year: "))
# month=int(input ("Enter month: "))
# day=int(input ("Enter day: "))
# mydate = datetime.date(year, month, day)
# print(mydate)

# today = datetime.date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)

# now() ro current date and time
# datetime.datetime.now()

# today = datetime.datetime.now()
# print(today)

# timedelta
from datetime import timedelta

dA = datetime.date.today()
dA += timedelta(days = 15)
print(dA)

dB = datetime.date.today()
dB -= timedelta(days = 15)
print(dB)


