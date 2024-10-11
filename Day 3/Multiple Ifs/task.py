# Multiple If's

# If / elif / else
# if <condition 1 is true>
#     <do A>
# elif <condition 2 is true>
#     <do B>
# else
#     <do C>

# Nested if statements
# if <condition 1 is true>
#     <do A>
#     if <condition 2 is true>
#         <do B>
#         if <condition 3 is true>
#             <do C>

# Multiple if statements
# if <condition 1 is true>
#     <do A>
# if <condition 2 is true>
#     <do B>
# if <condition 3 is true>
#     <do C>

# ==> Course Content <==
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Initialize bill
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    print("")

    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult ticket are $12.")

    # Charge $3 if yes
    wants_photo = input("Do you want to have a photo take?, Type y for Yes and n for No. ")
    if wants_photo == "y":
        bill += 3

        # If this same level with "bill", it will only execute after user type "y", if not then it skip.
    # If this same level with "if", it will execute after "if" statement are completed.
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
