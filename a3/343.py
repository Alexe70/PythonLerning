f = open("C:\\Projects\\pythonLearning\\PythonLerning\\a3\\StudentsPerformance.csv") 
count = 0
flag = True
list = []

scope = 0
for student in f:
    string = student.split(',')
    if string[0] == '"gender"':
        continue
    else:
    
        lunch = string[3][1:-1]
        #gender = string[0][1:-1]
        scope = int(string[-1][1:-2])
        scope1 = int(string[-3][1:-1])

        if lunch != 'standard':
            list.append(scope)
    
avgScope = sum(list)/len(list)


print(avgScope)