# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

#Changes Made by:Daniel Fernandes(M00908452)

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: ")) #all inputs have to be integer values, changed variable name from exam_3 to exam_three

grades = [exam_one, exam_two, exam_three] #list missing "," in between
sum = 0
for grade in grades: #varible name for the list in the loop corrected "grades"
  sum = sum + grade

avg = sum / len(grades) #len(grades) corrected error in list name

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #was missing a colon
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"    #mismatch in inverted comma
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:       #else statement was missing
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F":  #comparison operator == was missing and error in variable name 
    print("Student is failing.") #print statement missing parrentheses
else:
    print("Student is passing.") #print statement missing parrentheses
