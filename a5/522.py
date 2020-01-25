def get_median(list):
    list = sorted(list)
    if len(list)%2 != 0:
        return list[len(list)//2]
    else:
        a = list[len(list)//2-1]
        b = list[len(list)//2]
        return int((a+b)/2)
l = [3, 7, 9, 3]
med = get_median(l)
print(med)