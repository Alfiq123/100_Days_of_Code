# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M or L: L
# Do you want pepperoni on your pizza? Y or N: Y
# Do you want extra cheese? Y or N: N
# Your final bill is: $28.

# Python Pizza Project
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

# Small Size
if size == "S":
    bill = 15
    # Pepperoni for small size
    if pepperoni == "Y":
        bill += 2
    # Cheese for Medium
    if extra_cheese == "Y":
        bill += 1

# For Medium Size
elif size == "M":
    bill = 20
    # Pepperoni for Medium
    if pepperoni == "Y":
        bill +=3
    # Cheese for Medium
    if extra_cheese == "Y":
        bill += 1

# For Large Size
elif size == "L":
    bill = 25
    # Pepperoni for Large
    if pepperoni == "Y":
        bill += 3
    # Cheese for Large
    if extra_cheese == "Y":
        bill += 1

print("==============================")
print("PYTHON PIZZA CORPORATION")
print("==============================")
print(f"Your pizza size: {size}")
print(f"Are you have pepperoni?: {pepperoni}")
print(f"Are you have extra cheese?: {extra_cheese}")
print("==============================")
print(f"Your final bill is: ${bill}.")

# ===--- Python Course Solution ---=== #

# Python Pizza Project
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

# Pizza Price
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Please Enter a Valid Size!")

# Pepperoni Charge
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: {bill}.")
