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
