num = int(input("What number do you want to take the square root?: "))
num_range = list(range(num + 1))
ans = ""
for x in num_range:
    if num == x * x:
        ans += str(x)
print(ans)



