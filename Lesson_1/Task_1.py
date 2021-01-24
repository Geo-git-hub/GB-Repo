def return_format(num_to_format):
    if len(str(num_to_format)) == 1:
        num_to_format = "0" + str(num_to_format)
    return num_to_format


user_seconds = input("Укажите время в секундах: ")
while not user_seconds.isdigit():
    user_seconds = input("Укажите время в секундах (введите целое число): ")
user_seconds = int(user_seconds)
seconds = return_format(user_seconds % 60)
minutes = return_format((user_seconds // 60) % 60)
hours = (user_seconds // 60) // 60
print(f"\nВы ввели: {user_seconds} секунд, что составит {hours}:{minutes}:{seconds} ")
