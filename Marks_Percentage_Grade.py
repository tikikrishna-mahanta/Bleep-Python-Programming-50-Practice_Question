marks = []

for i in range(5):
    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)