"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
my_list = [4, 1, 1, 7, 3, 3, 6, 6]
number = int(input(f"Имеем рейтинг: {my_list}, ведите новый элемент рейтинга: "))
step = len(my_list)-1
action = 0
while step > -1:
    if int(my_list[step]) == number:
        action = 1
        break
    step -= 1

if action == 0:
    my_list.append(number)
elif action == 1:
    my_list.insert(step, number)
print(f"Рейтинг после магии: {my_list}")