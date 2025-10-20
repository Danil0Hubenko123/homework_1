# Завдання 1
from datetime import datetime
year = 2025
month = 5
day = 16

def get_days_from_today(days_since=0):
    # Поточна дата
    current_date = datetime.now()
    print(f"Поточна дата: {current_date.strftime('%Y-%m-%d')}")
    
    # Фіксована дата
    fixed_date = datetime(year, month, day)
    print(f"Фіксована дата: {fixed_date.strftime('%Y-%m-%d')}")

    # Розрахунок кількості днів
    days_since = (current_date - fixed_date).days
    if days_since > 0:
        print(f"Пройшло {abs(days_since)} днів з фіксованої дати")
    
    return days_since

get_days_from_today(days_since = 0)
