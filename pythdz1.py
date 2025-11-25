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