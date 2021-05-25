days = ['mon','tue','wed','thu','fri','sat','sun']

workdays = days.copy()
workdays.remove('sun')
workdays.remove('sat')
print(workdays,"ID variable: ", id(workdays))
print("------------------------------------------------------")
print(days,"ID variable: ", id(days))
