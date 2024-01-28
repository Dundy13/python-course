from datetime import date
today = date.today()

date1 = today.strftime('%d-%m-%Y')
print('date1=', date1)


from datetime import datetime

c = datetime.now()

current_time = c.strftime("%H:%M:%S")
print('Çurrent Date and Time is:', c)


formatted_date = c
print('Форматирана дата:', formatted_date)

# past_date = datetime(2020, 9, 5)
# is_past = date1 > past_date
past = c.strftime("05/09/22")
print(past)
if past == c.strftime("%D"):
    print("Todays date is after", past)
else:
    print("Todays date is after", past)