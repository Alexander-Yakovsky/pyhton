# Задание 1
vozrast = int(input("Введите ваш возраст: "))
rost = int(input("Введите ваш рост: "))
pol = input("Напишите ваш пол: ")
print("Отлично, ваш пол",pol,",ваш возраст",vozrast,"и ваш рост сейчас",rost,"сантиметров.")

# Задание 2

seconds = int(input("Введите время в секундах: "))

hour = seconds // 3600
# Если больше 24 часов
if hour > 24:
    print("Введенное время в секундах привышает сутки")
    raise SystemExit

minutes = seconds // 60

hour %= 24
minutes %= 60
seconds %= 60

print("Итого в часах:",hour,":",minutes,":",seconds,".")

# Задание 3

n = int(input("Введите число:"))
summ = int(n+n*11+n*111)

print("Cумма всех чисел равна",summ)

# Задание 4

viruchka = int(input("Введите выручку:"))
izderzhki = int(input("Введите издержки:"))

# Определяем прибыль
pribul = viruchka - izderzhki

if pribul > 0:
    print("Ваша прибыль больше издержек и это круто")
elif pribul < 0:
    print("Ваша прибыль меньше издержек и это плохо")

# Определяем соотношение выручки
sootnoshenie = viruchka / pribul

if sootnoshenie < 0:
    print("Ваше соотношение меньше прибыли к выручке меньше нуля")
elif sootnoshenie > 0:
    print("Ваше соотношение прибыли к выручке равно",sootnoshenie,)

# Расчет прибыли на человека
numder_s = int(input("Теперь введите численность сотрудников:"))

pribul_s = pribul / numder_s
print("Прибыль на человека равна",pribul_s,)


# Задание 5
a = 2 # первый результат спорцмена
b = 3 # нужно найти этот результат спорцмена
day = 0 # номер дня

while b - a > 0:
    a = a + (a * 0.03) # вычисляем рассояние в км за новый день
    day += 1
    print("День",day,"в километрах",a,"км")
