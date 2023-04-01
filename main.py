import calendar

print ('Календарь\n')
year = (int)(input('Введите год: '))
month = (int)(input('Введите месяца: '))
print(calendar.month(year, month))
