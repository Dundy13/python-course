number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > number2:
    print(number1)
elif number1 <= number2:
    print(number2)



age = int(input("Въведете възраст:"))
gender = int(input("Въведете пол(m за мъж и f за жена): "))

if gender == 'm':
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
elif gender == 'f':
    if age >= 16:
        print("Ms.")
    else:
        print("Miss.")
else:
    print("Невалиден пол")



number = int(input("Въведете цяло число :"))
if number % 2 == 0:
    print("even")
else:
    print("odd")



day_of_week = input("Enter day of the week:")

match day_of_week:
    
    case "Monday":
        print("12")
    case "Tuesday":
        print("12")
    case "Wednesday":
        print("14")
    case "Thursday":
        print("14")
    case "Friday":
        print("12")
    case "Saturday":
        print("16")
    case "Sunday":
        print("16")
    case _:
        print("Invalid day of the week")





days_of_week = {
    'Monday': 0,
    'Tuesday': 0,
    'Wednesday': 0,
    'Thursday': 0,
    'Friday': 0,
    'Saturday': 0,
    'Sunday': 0
}

n = int(input("Въведете брой дни: "))
for _ in range(n):
        day = input("Въведете ден от седмицата: ")

if day in days_of_week:
    days_of_week[day] += 1
else:
    print("Невалиден ден от седмицата.")

str:
for day, count in days_of_week.items():
            if count > 0:
                print(f"{day} - {count} times")
except ValueError:
print("Моля, въведете число за броя дни.")