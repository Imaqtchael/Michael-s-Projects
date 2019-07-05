
stone = open("Amethyst.txt", "a")
ans = input("What do you want to put in the TEXT file?: ")
stone.write("\n" + ans)
stone.close()
stone2 = open("Amethyst.txt", "r")
print(stone2.read())
stone2.close()