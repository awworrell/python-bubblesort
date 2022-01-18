students = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh",39]]


for student in range(0,len(students)-1):          
    for sorted_student in range(0,len(students)-1):
        temp=students[sorted_student]                         
        if students[sorted_student][1] > students[sorted_student+1][1]:
            print(students[sorted_student])
            students[sorted_student] = students[sorted_student+1]
            students[sorted_student+1] = temp

print(students[-4][0])
print(students[-3][0])






            
    



