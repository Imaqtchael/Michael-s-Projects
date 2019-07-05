ask = int(input("Enter a number: "))
range = list(range(1, ask + 1))
divlist = []
for x in range:
    if ask % x == 0:
        divlist.append(x)
print(divlist)