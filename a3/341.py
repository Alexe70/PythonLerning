f = open("C:\\Projects\\pythonLearning\\PythonLerning\\a3\\StudentsPerformance.csv") 
count = 0
flag = True
list = []
for student in f:
    string = student.split(',')
    parental = string[1][1:-1]
    for p in list:
        if parental == p:
            flag = False
            break
        else:
            flag = True
    if flag == True:
        list.append(parental)
        flag = False
        count += 1
print(count)