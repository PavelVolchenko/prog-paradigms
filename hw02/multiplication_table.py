# Процедурная парадигма — возможность повторного переиспользования кода,
# так как он упакован в процедуры, которые можно сохранить,
# а потом вызвать откуда угодно
def print_table(columns):
    for i in range(1, columns + 1):
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j}")
        print()


columns = int(input("Enter the number of columns table: "))

# Структурная парадигма — возможность быстрой проверки кода на работоспособность
for i in range(1, columns + 1):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print()
