user_number = input("Введите число: ")
while not user_number.isdigit():
    user_number = input("Введите число: ")
user_number_1 = int(user_number)
user_number_2 = int(str(user_number) + str(user_number))
user_number_3 = int(str(user_number_2) + str(user_number_1))
print(f"\nОтвет: {user_number_1 + user_number_2 + user_number_3}")