raw_list = [2, 8, 10, 23, 64, 49, 11, 52, 71, 14]
lenghtRaw_list = len(raw_list)
my_list = []
x_min = min(raw_list)
x_max = max(raw_list)

for index in range(lenghtRaw_list):
  
  if index+1%2 != 0:
     my_list.append(raw_list[index]*x_max)
  else:
     my_list.append(raw_list[index]*x_min)
    
  
result = max(my_list)
#print(str(result))

# Введите свое решение здесь
         