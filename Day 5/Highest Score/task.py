# Highest Score
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
print(max(student_scores))

print("")

# Sums the items of an iterator
summary = sum(student_scores)
print(summary)

print("")

summ = 0
for score in student_scores:
    summ += score

print(summ)

print("")

# PAUSE 1
# Explanation:
# 1. If "score2" greater than "maximum"
# 2. Set "score2" to the "maximum" value
maximum = 0
for score2 in student_scores:
    if score2 > maximum:
        maximum = score2
print(maximum)

print("")

the_scores = [11, 79, 30, 34, 74, 69, 75, 44, 46, 27, 47, 1, 48, 96, 97, 6, 37, 57, 32, 54, 7, 88, 77, 2, 85]
maxed = 0
for the_score in the_scores:    # Assign "the_score"
    if the_score > maxed:       # If "the_score" greater than "maxed"
        maxed = the_score       # Set "the_score" to the "maxed" value
print(maxed)
