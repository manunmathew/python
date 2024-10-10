import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

a = calendar.month(year,month)
print(a)

year = int(input("Enter the year: "))
a = calendar.calendar(year)
print(a)

year = int(input("Enter the year: "))
a = calendar.isleap(year)
print(a)
a = calendar.TextCalendar(calendar.SUNDAY)
print(a.formatyear(year))
print(a.formatmonth(year, month))
