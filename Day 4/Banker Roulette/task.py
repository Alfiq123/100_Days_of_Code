import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

checkmate = random.randint(0, 4)

# Option 1 - Very Useful
# .choice - Used for pick a random item from the list
print(random.choice(friends))

print("")

# Option 2 - Useful
print(friends[checkmate])

print("")

# Option 3 - Least Useful
if checkmate == 0:
    print(friends[0])
elif checkmate == 1:
    print(friends[1])
elif checkmate == 2:
    print(friends[2])
elif checkmate == 3:
    print(friends[3])
else:
    print(friends[4])
