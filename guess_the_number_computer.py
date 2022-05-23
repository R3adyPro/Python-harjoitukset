import random

used_numbers = []


the_number = random.randrange(1,100)


while True:
    num = random.randrange(1, 100)
    if num == the_number:
        print('The ringht number is', num)
        print(the_number)
        print(used_numbers)
        break
    elif num in used_numbers:
        continue
    elif num not in used_numbers:
        used_numbers.append(num)