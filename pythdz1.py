import random
from colorama import Fore
def guess_number_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print('try to guess the number from 1 to 100')
    while True:
        try:
            guess = int(input('ur guess: '))
            attempts += 1
            if guess < secret_number:
                print(Fore.BLUE + 'too low' + Fore.RESET)
            elif guess > secret_number:
                print(Fore.RED + 'too high' + Fore.RESET)
            else:
                print(Fore.GREEN + 'u guessed right' + Fore.RESET)
                print(f'number of attempts: {attempts}')
        except ValueError:
            print('please enter a number')
'''- Импортируются модули random и colorama для цветного вывода текста.
- Программа генерирует случайное число от 1 до 100.
- Пользователь пытается угадать число, вводя предположения.
- За каждый ввод считается попытка.
- Если ввод меньше загаданного числа, выводится сообщение "слишком мало" синим цветом.
- Если больше, выводится "слишком много" красным цветом.
'''
import time
import os


def main():
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            current_time = time.strftime("%H:%M:%S")
            print(current_time)
    except KeyboardInterrupt:
        print("\nПрограмма остановлена пользователем.")
if __name__ == '__main__':
    main()
'''- Импортируются модули time и os.
- В бесконечном цикле программа очищает экран (используя команду cls для Windows и clear для Unix-систем).
- На экран выводится текущее время в формате часы:минуты:секунды.
- Цикл прерывается при нажатии Ctrl+C, при этом выводится сообщение о остановке программы пользователем.
'''
import requests
url = input("Введите URL: ")
try:
    response = requests.get(url)
    if 200 <= response.status_code < 400:
        print(f"Сайт доступен! Код ответа: {response.status_code}")
    elif response.status_code >= 400:
        print(f"Сайт недоступен! Код: {response.status_code}")
'''- Импортируется библиотека requests для работы с HTTP-запросами.
- Пользователь вводит URL сайта.
- Выполняется GET-запрос к введённому адресу.
- Если код ответа сервера от 200 до 399 включительно, выводится сообщение о доступности сайта и код ответа.
- Если код ответа 400 или выше, выводится сообщение о недоступности сайта и код ошибки.
'''
