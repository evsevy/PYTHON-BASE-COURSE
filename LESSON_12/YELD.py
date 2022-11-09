# ОДНОПОТОЧНАЯ РЕКУРСИЯ С ПРЕРЫВАНИЕМ

import time

# Программа на Python для генерации степеней 2
# от 2 до 256
def get_next_num():
    n = 2
  
    # Бесконечный цикл для генерации степеней 2
    while True:
        yield n
        n *= 2  # При последующем обращении к 
                # get_next_num() выполнение
                # продолжится отсюда 
  
# Код для проверки get_next_num()
for num in get_next_num():
    if num > 1200560:
         break    
    print(num)
    time.sleep(5)
