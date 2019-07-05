import random
set1 = list((range(1, random.randint(1, 10 ))))
set2 = list(range(1, random.randint(1, 10 )))
like = []
for num in set1:
    if num in set2:
        like.append(num)
print(like)