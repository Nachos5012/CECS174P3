#A
num=80
while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1
#B
num = 100
while num >= 80:
    if num % 2 == 0:
        print(num)
    num -= 1
#c
while True:
    try:
        lower_limit = int(input("Enter the lower limit (a positive integer): "))
        if lower_limit < 0:
            print("Please enter a positive integer for the lower limit.")
            continue
        upper_limit = int(input("Enter the upper limit (a positive integer): "))
        if upper_limit < 0:
            print("Please enter a positive integer for the upper limit.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer.")

num = upper_limit
while num >= lower_limit:
    if num % 2 == 0:
        print(num)
    num -= 1

#While2
#A
while True:
    try:
        lower_limit = int(input("Enter the lower limit (a positive integer): "))
        if lower_limit < 0:
            print("Please enter a positive integer for the lower limit.")
            continue
        upper_limit = int(input("Enter the upper limit (a positive integer): "))
        if upper_limit < 0:
            print("Please enter a positive integer for the upper limit.")
            continue
        if upper_limit < lower_limit:
            lower_limit, upper_limit = upper_limit, lower_limit
        break
    except ValueError:
        print("Please enter a valid integer.")

num = lower_limit
while num <= upper_limit:
    if num % 2 == 0:
        print(num)
    num += 1
#B

while True:
    try:
        lower_limit = int(input("Enter the lower limit (a positive integer): "))
        if lower_limit < 0:
            print("Please enter a positive integer for the lower limit.")
            continue
        upper_limit = int(input("Enter the upper limit (a positive integer): "))
        if upper_limit < 0:
            print("Please enter a positive integer for the upper limit.")
            continue
        if upper_limit < lower_limit:
            lower_limit, upper_limit = upper_limit, lower_limit
        step = int(input("Enter the step value between 1 and 10"))
        if step < 1 or step > 10:
            print("Please enter a step value between 1 and 10")
            continue
        break
    except ValueError:
        print("Please enter a valid integer.")

num = upper_limit
while num >= lower_limit:
    if num % 2 == 0:
        print(num)
    num -= step

#c
while True:
    try:
        while True:
            lower_limit = int(input("Enter the lower limit (a positive integer): "))
            if lower_limit < 0:
                print("Please enter a positive integer for the lower limit.")
                continue
            upper_limit = int(input("Enter the upper limit (a positive integer): "))
            if upper_limit < 0:
                print("Please enter a positive integer for the upper limit.")
                continue
            if upper_limit < lower_limit:
                lower_limit, upper_limit = upper_limit, lower_limit
            step = int(input("Enter the step value between 1 and 10 (inclusive): "))
            if step < 1 or step > 10:
                print("Please enter a step value between 1 and 10 (inclusive).")
                continue
            break
        num = upper_limit
        while num >= lower_limit:
            if num % 2 == 0:
                print(num)
            num -= step
    except ValueError:
        print("Please enter a valid integer.")
    
    run_again = input("Do you want to run the code again? (yes/no): ")
    if run_again.lower() != 'yes':
       break
        





