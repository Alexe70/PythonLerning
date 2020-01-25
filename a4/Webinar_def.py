from datetime import datetime

with open ('test_taxi.csv') as f:
    next(f)
    counter = 0
    for line in f:
        counter += 1
        print(line)
        if counter == 5: break