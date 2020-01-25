print(list(map(abs, [10,  -1, 42, -73]))[3])


values = [1, 2, 3]
vectors = [(10, 3), (4, 5), (6, 7)]

map(lambda x: x+2, [1, 2, 3])

map(lambda vec: (vec[0]**2 + vec[1]**2)**0.5, vectors)

map(lambda x, y: x + y, values)