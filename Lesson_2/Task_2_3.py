"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
 Напишите решения через list и через dict."""

# ================== реализация через словари ============================================
user_input = input("Введите месяц в виде целого числа от 1 до 12: ")

while not user_input.isdigit() or int(user_input) < 1 or int(user_input) > 12:
    user_input = input("Введите месяц в виде целого числа от 1 до 12: ")

user_input = int(user_input)
dict_month = {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето", 9: "осень",
              10: "осень", 11: "осень", 12: "зима"}
print(f"Введённому значению : {user_input}, соответствует время года: {dict_month.get(user_input)} ")

# =============== реализация через списки ====================================================

user_input = input("Введите месяц в виде целого числа от 1 до 12: ")

while not user_input.isdigit() or int(user_input) < 1 or int(user_input) > 12:
    user_input = input("Введите месяц в виде целого числа от 1 до 12: ")

user_input = int(user_input)
list_month = [["зима", 1, 2, 12], ["весна", 3, 4, 5], ["лето", 6, 7, 8], ["осень", 9, 10, 11]]
for i in range(len(list_month)):
    for j in range(len(list_month[i])):
        if list_month[i][j] == user_input:
            break
    else:
        continue
    break
print(f"Введённому значению : {user_input}, соответствует время года: {list_month[i][0]} ")
