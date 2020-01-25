number = 56.257
sum = 0
string =str(number)
drobIndex = string.find('.')
drob = string[drobIndex+1:]
for i in drob:
    sum += int(i)

print(sum)
