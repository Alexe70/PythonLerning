values = [4, 8, 15, 16, 23, 42]
mean = 18

result = list(map(lambda x: x - 18, values))

#print (result)

def normalize(numbers,mean=0,std=1):
    list = []
    for n in numbers:
        list.append(int((n - mean)/std))
    return list

def show_keys(**kwargs):
    print(' '.join(kwargs.keys()))

show_keys(verbose=True, mode='constant')