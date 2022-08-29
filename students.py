"""Students are entering a class one by one. Get their names as they enter. At the end of the class, Students
leave the class in reverse order (the student who came last leaves first). Call the student using their name and ask about 
their mark in the class. Calculate the class average. """

enterStudents = []
totalMarks = 0
classStrength = int(input("enter class strenght: "))
for enter in range (0, classStrength):
    studentsName = input("enter name: ")
    enterStudents.append(studentsName)
firstAttendance = enterStudents
for exit in range (0, int(classStrength/2)):
    n = enterStudents[exit]
    enterStudents[exit] = enterStudents[classStrength-exit-1]
    enterStudents[classStrength-exit-1] = n
lastAttendance = enterStudents
print('firstAttendance', firstAttendance)
print('lastAttendance', lastAttendance)

if (firstAttendance[classStrength -1] == lastAttendance[classStrength -1]):
    print("Hey", firstAttendance[classStrength -1], "what about your marks?")
    subjectCount = int(input("how many subject do you have? "))
    for subject in range (0, subjectCount):
        print("In subject", subject + 1, "I have scored")
        subjectMarks = int(input())
        totalMarks += subjectMarks
print("my total marks is: ", totalMarks)
print("my average marks is: ", int(totalMarks / subjectCount))
