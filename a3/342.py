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
        scope = int(string[-3][1:-1])
        list.append(scope)
    
avgScope = max(list)


print(avgScope)