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

