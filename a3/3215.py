basic_word = 'сос'
inverted_word = basic_word[len(basic_word)::-1]
print(inverted_word)
if(basic_word == inverted_word):
    print('Слово "{}" является палиндромом' .format(basic_word))
else:
    print('Слово "{}" - это не палиндром' .format(basic_word))
     