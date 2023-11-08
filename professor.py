import random
import sys

def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        s = input("Level: ")
        if s in ('1', '2', '3'):
            s = int(s)
            return s

def generate_integer(level):
    if level == 1:
        userscore = 0
        for num in range(1, 11):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            userscore = calculate(x, y, userscore, max_wrong_attempts=3)
        print("Score:", userscore)
        sys.exit()

    elif level == 2:
        userscore = 0
        for num in range(1, 11):
            x = random.randint(10, 99)
            y = random.randint(10, 99)
            userscore = calculate(x, y, userscore, max_wrong_attempts=3)
        print("Score:", userscore)
        sys.exit()

    elif level == 3:
        userscore = 0
        for num in range(1, 11):
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            userscore = calculate(x, y, userscore, max_wrong_attempts=3)
        print("Score:", userscore)
        sys.exit()

def calculate(x, y, userscore, max_wrong_attempts):
    ans = x + y
    wrong_attempts = 0

    while wrong_attempts < 3:
        userinput = input(f"{x} + {y} = ")

        if userinput.isnumeric():
            userinput = int(userinput)
            if userinput == ans:
                userscore += 1
                break
            else:
                print("EEE")
                wrong_attempts += 1
        else:
            print("EEE")
            wrong_attempts += 1
        
        if wrong_attempts == 3:
            print(f"{x} + {y} = {ans} ")
    return userscore

if __name__ == "__main__":
    main()
