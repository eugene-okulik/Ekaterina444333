import random


salary = int(input('enter your salary: '))
bonus1 = [True, False]


def final_salary():
    bonus = random.choice(bonus1)
    bonus_count = random.randint(1000, 5000)
    if bonus is True:
        print(f"{salary}, {bonus} - '${salary + bonus_count}'")
    else:
        print(f"{salary}, {bonus} - '${salary}'")


final_salary()
