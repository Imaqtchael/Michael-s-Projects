
def raise_to_power():
    result = 1
    for x in range(int(pow_num)):
        result = result * int(base_num)
    print(result)


err = True
out = 0
while err:
    try:
        base_num = float(input("Enter your base number: "))
        out += 1
        pow_num = float(input("Number you want to raise it: "))
        raise_to_power()
        err = False
    except ValueError:
        if out > 0:
            print("Invalid input!")
            err_2 = True
            while err_2:
                try:
                    pow_num = float(input("Enter your second number: "))
                    raise_to_power()
                    err_2 = False
                    err = False
                except ValueError:
                    print("Invalid input!")
        else:
            print("Invalid input!")

