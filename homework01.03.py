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
    else:
        sanitized = '+38' + sanitized
        return sanitized

print("--- Нормалізація телефонів ---")
for num in raw_numbers:
    normalized = normalize_phone(num)
    print(f"{normalized}")

