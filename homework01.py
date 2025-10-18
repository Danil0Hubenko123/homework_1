# Завдання 1
def get_days_from_today(days_since):
    from datetime import datetime
    # Перевірка на правильність введення року
    while True:
        try:
            year_elect = int(input("Введіть рік: "))
            if year_elect < 1 or year_elect > 9999:
                print("Введіть правильний рік: ")
                continue
            break
        except ValueError:
            print("Введіть ціле число: ")
    # Перевірка на правильність введення місяця
    while True:
        try:
            month_elect = int(input("Введіть місяць: "))
            if month_elect < 1 or month_elect > 9999:
                print("Введіть правильний місяць: ")
                continue
            break
        except ValueError:
            print("Введіть ціле число: ")
    # Перевірка на правильність введення дня        
    while True:
        try:
            day_elect = int(input("Введіть день: "))
            if day_elect < 1 or day_elect > 9999:
                print("Введіть правильний день: ")
                continue
            break
        except ValueError:
            print("Введіть ціле число: ")        
        
    # Встановлення дати 
    data_elect = datetime(year_elect, month_elect, day_elect)

    # Поточна дата
    current_date = datetime.today()

    # Розрахунок кількості днів
    days_since = current_date.toordinal() - data_elect.toordinal()
    print(f"Днів між датою і сьогоднішнім {days_since}")
    
    return days_since

get_days_from_today(days_since = 0)

# Завдання 2
def get_numbers_ticket(min, max, quantity):
    # Задані параметри
    min = 1
    max = 1000
    quantity = 6
    import random
    lottery_numbers = []
    # Розрахунок унікальних чисел
    if quantity > (max - min + 1):
        print("Помилка: Кількість унікальних чисел, яку потрібно згенерувати, більша за діапазон.")
        return []
    while len(lottery_numbers) < quantity:
        numbers = random.randint(min, max) 
        if numbers not in lottery_numbers:
            lottery_numbers.append(numbers)     
    lottery_numbers.sort()        
    return lottery_numbers    
# Вивід лотерейних чисел
lottery_numbers = get_numbers_ticket(min=None, max= None, quantity=None)
print("Ваші лотерейні числа:", lottery_numbers)

# Завдання 3
raw_numbers = [
    "067\t123 4567",         
    "(095) 234-5678\n",       
    "+380 44 123 4567",       
    "380501234567",           
    "    +38(050)123-32-34",  
    "     0503451234",         
    "1234567890",             
    "+44 1234567890",         
]        

def normalize_phone(phone_number, raw_numbers=None):
    import re
    sanitized = re.sub(r'[^\d+]', '', phone_number)
    if sanitized.startswith('+'):
        if not sanitized.startswith('+38'):
            if sanitized.startswith('+0'):
                sanitized = '+38' + sanitized[1:]
            return sanitized
        return sanitized
    elif sanitized.startswith('380'):
        sanitized = '+' + sanitized
        return sanitized   
    elif sanitized.startswith('0'):
        sanitized = '+38' + sanitized
        return sanitized
    else:
        sanitized = '+38' + sanitized
        return sanitized

print("--- Нормалізація телефонів ---")
for num in raw_numbers:
    normalized = normalize_phone(num)
    print(f"{normalized}")

# Завдання 4

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},       
# добавив трохи більше 
    {"name": "Bob Johnson", "birthday": "1988.10.28"}, 
    {"name": "Charlie Wilson", "birthday": "1995.10.29"}, 
    {"name": "Eve Davis", "birthday": "1998.10.30"}, 
    {"name": "Grace Lee", "birthday": "1991.10.20"},
]

def get_upcoming_birthdays(users):
    from datetime import datetime, timedelta
    today = datetime.now().date()
    seven_days_from_now = today + timedelta(days=7)
    upcoming_birthdays = []
    for user in users:
        try:           
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except ValueError:
            print(f"Помилка формату дати для користувача {user['name']}. Пропускаємо.")
            continue
        birthday_this_year = birthday.replace(year=today.year)        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)        
        if today <= birthday_this_year < seven_days_from_now:            
            congratulation_date = birthday_this_year           
            day_of_week = birthday_this_year.weekday()            
            if day_of_week >= 5: 
                if day_of_week == 5:
                    days_to_add = 2
                else: 
                    days_to_add = 1                
                congratulation_date = birthday_this_year + timedelta(days=days_to_add)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    return upcoming_birthdays

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні (відповідно до поточної дати):")
print(upcoming_birthdays)

