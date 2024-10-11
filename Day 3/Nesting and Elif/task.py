# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("Enter your age: "))
#     if age < 12:
#         print("You must pay: $5")
#     elif age <= 18:
#         print("You must pay: $7")
#     elif age > 18:
#         print("You must pay: $12")
# else:
#     print("Sorry you have to grow taller before you can ride.")

print("")

# maths_score = int(input("Enter your math score: "))
# english_score = int(input("Enter your english score: "))
#
# if maths_score >= 90:
#     if english_score >= 90:
#         print("You're good at everything")
#     else:
#         print("You're good at maths")
# if english_score >= 90:
#     print("You're good at english")

weight = int(input("Weight: "))
height = float(input("Height: "))

bmi = weight / (height ** 2)
print(bmi)

if bmi < 18.5:
    print("Underweight")
else:
    if bmi >= 18.5:
        print("Normal Weight")
    else:
        if bmi < 25:
            print("Normal Weight")
        else:
            print("Overweight")
