a = float(input("Введіть перше число : "))
b = float(input("Введіть друге число : "))
c = float(input("Введіть третє число : "))
d = float(input("Введіть четверте число : "))

results = [
    a + b,
    a - b,
    a * b,
    a / b,
    a ** b,
    a // b,
    a % b
]

print(f"Кількість елементів у списку: {len(results)}")
print("Парні елементи списку:")
for number in results:
    if number % 2 == 0:
        print(number)

results[1], results[4] = results[4], results[1]
print("Оновлений список:", results)

name = input("Введіть ваше прізвище та ім'я: ")
print("Виконавець даної лабораторної роботи:", name)
print("Висновки по лабораторній роботі:")
print("Ця лабораторна робота допомогла мені навчитися працювати з основними арифметичними операціями в Python.")
