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
