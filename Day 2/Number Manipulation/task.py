bmi = 84 / 1.65 ** 2
print(bmi)

# Number Manipulation
# Flooring a Number
print(int(bmi))

# Rounding a Number - Using (round) Function
# round(number, n-digit)
print(round(bmi))
print(round(bmi, 2))
print(round(bmi, 3))
print(round(52.1234567, 3))

print("")

# Assignment Operators
# += : ...+...
# -= : ...-...
# *= : ...*...
# /= : .../...

highscore = 1280
highscore += 64
print(highscore)

print("")

# f-String = Insert a variable or an expression into a string.
# "String{Variable}" - "...{...}"
# "String{Variable}String{Variable}" - "...{...}...{...}"
score1 = 640
score2 = 1280
winner = True

print(f"Your actual score 1 is {score1}, and your score 2 is {score2}. So, your winner are: {winner}")
