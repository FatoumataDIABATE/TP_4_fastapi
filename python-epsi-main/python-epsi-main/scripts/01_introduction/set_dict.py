import random

r = random.Random()


random_ints = [r.randint(0, 100) for _ in range(50)]

goal = [40, 67, 23]

for r_i in random_ints:
    for g in goal:
        if r_i == g:
            print("FOUND", r_i)

print("*" * 100)

set_random_ints = set(random_ints) # 50 elements
set_goal = set(goal) # 3 elements

for r_i in set_goal:
    if r_i in set_random_ints:
        print("FOUND", r_i)

print("*" * 100)

print(set_random_ints & set_goal)