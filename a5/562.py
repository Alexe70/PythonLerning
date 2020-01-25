def count_letters(sentence, average=False):
    words = sentence.split(' ')
    if average:
        count_list = []
        avr = 0
        for word in words:
            count_list.append(len(word))
        avr = sum(count_list)/len(count_list)
        return avr
    else:
        count = 0
        for word in words:
            count += len(word)
        return count

print(count_letters('fg fg', True))