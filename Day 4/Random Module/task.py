import random
# Random Module
# Functions for integers

# random.randrange(stop)
# random.randrange(start, stop[, step])

# Returns a random integer between a and b (both inclusive).
random_int = random.randint(1, 20) / 3
print(random_int)

print("")

# Returns a random floating-point number in the range [0.0, 1.0).
random_numbers = random.random() * 5
print(random_numbers)

print("")

# Returns a random floating-point number between a and b.
random_float = random.uniform(1, 5) + 12
print(random_float)

print("")

check = random.randint(0, 1)
if check == 0:
    print("head")
else:
    print("tail")
print(check)
