base_list = list(map(int, input("Введите значения элементов списка:").split()))
for number in base_list:
    if number == 237:
        break
    elif number % 2 == 0:
        print(number)

