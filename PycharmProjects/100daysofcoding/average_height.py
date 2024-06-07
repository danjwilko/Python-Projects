# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total = 0
counter = 0
for heights in student_heights:
    total = total + int(heights)
    counter = counter + 1
result = round(total / counter)
print(f"total height = {total}\nnumber of students = {counter}\naverage height = {result}")

