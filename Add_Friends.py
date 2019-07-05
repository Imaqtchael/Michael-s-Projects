ans = [input("Type the name of your friends: \n"), input(), input(), input()]
friends = []
for x in ans:
    y = x.strip()
    friends.append(y)
while "" in friends:
    friends.remove("")
print(friends)
another_friend = input("Who do you wanna add from the list?: ")
af = another_friend.strip()
position = int(input("Where do you wanna place your new friend?: "))
friends.insert(position - 1, af)
while "" in friends:
    friends.remove("")
print(friends)