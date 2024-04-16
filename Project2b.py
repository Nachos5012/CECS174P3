import random

account_number = random.randint(1000, 9000)

while True:
    customer_code = ''
    while customer_code not in ['R', 'C', 'I']:
        customer_code = input("Enter customer code (R, C, or I): ").upper()
        if customer_code not in ['R', 'C', 'I']:
            print("Invalid input. Please enter R, C, or I")

    customer_name = input("Enter customer name: ")
    address = input("Enter customer address: ")
    phone_number = input("Enter customer phone number: ")

    beginning_reading = -1
    while(beginning_reading < 0 or beginning_reading > 999999999):
        beginning_reading = int(input("Enter beginning reading (between 0 and 999999999): "))
        if beginning_reading < 0 or beginning_reading > 999999999:
                print("Invalid input. Reading should be between 0 and 999999999.")

    ending_reading = -1
    while(ending_reading < 0 or ending_reading > 999999999):
        ending_reading = int(input("Enter ending reading (between 0 and 999999999): "))
        if ending_reading < 0 or ending_reading > 999999999:
                print("Invalid input. Reading should be between 0 and 999999999.")

    if ending_reading < beginning_reading:
           gallons = ((ending_reading + 1000000000) - beginning_reading)
    else:
           gallons = ending_reading - beginning_reading
    gallons_used = gallons / 10
       
    if customer_code == 'R':
        amount_billed = 5.00 + gallons_used * 0.0005
    elif customer_code == 'C':
        if gallons_used <= 4000000:
            amount_billed = 1000.00
        else:
            amount_billed = 1000.00 + (gallons_used - 4000000) * 0.00025
    else:
        if gallons_used <= 4000000:
            amount_billed = 1000.00
        elif gallons_used <= 10000000:
            amount_billed = 2000.00
        else:
            amount_billed = 2000.00 + (gallons_used - 10000000) * 0.00025
    
    print("--------------------Bill----------------------")
    print("Account Number:", account_number)
    print("Customer Name:", customer_name)
    print("Address:", address)
    print("Phone Number:", phone_number)
    print(f"Customer Code: {customer_code}")
    print(f"Beginning Reading: {beginning_reading:09}")
    print(f"Ending Reading: {ending_reading:09}")
    print(f"Gallons of Water Used: {gallons_used}")
    print(f"Amount Billed: ${amount_billed:.2f}")
    print("--------------------------------------------")
    
    choice = input("\nDo you want to perform new calculation? (Y/N): ").upper()
    if choice != 'Y':
        break
    else:
        account_number += 1
