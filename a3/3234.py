string = 'Тяжёлая интернет-зависимость - это когда ты выходишь из интернета, а он из тебя нет.'
replaceLitter = "-,."
for litter in replaceLitter:
    string = string.replace(litter,":)")
print(string)