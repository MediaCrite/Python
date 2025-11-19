list =[1, 3, 5, 3]
list.append(str)
list.insert(0, int)
list.append(list)
list.insert(2, tuple)
list.remove(1)
print(list.count(3))
print(list[5])
print(list)

dict = {str:int,
        tuple:list
        }
print(dict.pop(tuple))
print(dict.get(str))
print(dict)

numbers = [2, 5, 8, 15, 18, 23, 54, 32, 13, 24, 37, 56, 139, 89, 92, 101]
for num in numbers:
    if num == 139:
        break
    if num % 2 != 0:
        print(num)



list = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
filtered_numbers = []
other_sum = 0
print("Элементы, которые меньше 30 и делятся на 3 без остатка:")
for num in list:
    if num < 30 and num % 3 == 0:
        filtered_numbers.append(num)
    else:
        other_sum += num
print(filtered_numbers)
print(f"Сумма остальных элементов: {other_sum}")


def month_to_season(month):
    if not isinstance(month, int) or month < 1 or month > 12:
        return "Ошибка: номер месяца должен быть целым числом от 1 до 12"
    season_map = {
        12: "Зима", 1: "Зима", 2: "Зима",
        3: "Весна", 4: "Весна", 5: "Весна",
        6: "Лето", 7: "Лето", 8: "Лето",
        9: "Осень", 10: "Осень", 11: "Осень"
    }
    return season_map[month]
print(month_to_season(2))
print(month_to_season(5))