'''
Write an app to calculate Grades for students in each subject.
Mark > 90 is A, > 80 is B, > 70 is C, > 60 is D. anything less than 60 is fail.
Write a function that returns the grade for one subject for all the students in the class.
Also, print the class avg grade.
'''

numberOfStudents = int(input("number of students: "))
subjectName = input("enter the subject: ")
subjectMarks = []
subjectGrade = ['A', 'B', 'C', 'D', 'F']
grade = ''
averageMarks = 0
totalMarks = 0

def gradeCalCulation (marks, grade, students):
    totalMarks = 0
    if(numberOfStudents <= students):
        totalMarks += marks
        print('avg grade', grade)
        print('avg marks', round(totalMarks))
    else:
        print('grade', grade)

def calculationFunction(marks, students):
    if(numberOfStudents <= 100):
        if(numberOfStudents <= 100 and marks >= 90):
            grade = subjectGrade[0]
            gradeCalCulation(marks, grade, students)
        elif(numberOfStudents <= 90 and marks >= 80):
            grade = subjectGrade[1]
            gradeCalCulation(marks, grade, students)
        elif(numberOfStudents <= 80 and marks >= 70):
            grade = subjectGrade[2]
            gradeCalCulation(marks, grade, students)
        elif(numberOfStudents <= 70 and marks >= 60):
            grade = subjectGrade[3]
            gradeCalCulation(marks, grade, students)
        elif(numberOfStudents < 60):
            grade = subjectGrade[4]
            gradeCalCulation(marks, grade, students)

    # return grade

for students in range (numberOfStudents):
    print(subjectName)
    print("student", students + 1)
    marks = int(input("enter mark: "))
    calculationFunction(marks, students)
    totalMarks += marks
    averageMarks = totalMarks/numberOfStudents

calculationFunction(averageMarks, numberOfStudents+1)



'''
number of students: 5
enter the subject: Social Science
Social Science
student 1
enter mark: 88
grade B
Social Science
student 2
enter mark: 91
grade A
Social Science
student 3
enter mark: 78
grade C
Social Science
student 4
enter mark: 84
grade B
Social Science
student 5
enter mark: 50
grade F
avg grade C
avg marks 78
'''
