number = float(input("Въведете число: "))  

if -100 <= number <= 100 and number != 0:
    print("Yes")
else:
    print("No")


year = int(input("Въведете година: "))  

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Yes")
else:
    print("No")



    hour = int(input("Въведете час (цяло число): "))  
day = input("Въведете ден от седмицата (текст): ")

if 10 <= hour <= 18 and day.lower() in ['понеделник', 'вторник', 'сряда', 'четвъртък', 'петък', 'събота']:
    print("Офисът е отворен.")
else:
    print("Офисът е затворен.")



temperature = float(input("Въведете температура: ")) 

if temperature < 0:
    print("Студено")
elif 0 <= temperature <= 25:
    print("Умерено")
else:
    print("Топло")



    sum_amount = float(input("Въведете сума: "))  # Сума, въведена от потребителя
country = input("Въведете държава на доставка (текст): ")  # Държава, въведена от потребителя

if country == "България":
    delivery_cost = 0.02 * sum_amount
elif country == "Европа":
    delivery_cost = 0.05 * sum_amount
else:
    delivery_cost = 0.1 * sum_amount

total_amount = sum_amount + delivery_cost  # Изчисляване на крайната сума за плащане

print(f"Крайната сума за плащане, включително доставката: {total_amount:.2f}")


