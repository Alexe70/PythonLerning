proverb = 'Программисты - это устройства, преобразующие кофеин в код.'

new_proverb = ''
for index, litter in enumerate(proverb):
  if (index+1)%2 != 0:
      if index == 0:
        new_proverb += proverb[index+1::-1]
      else:
        new_proverb += proverb[index+1:index-1:-1]
print(new_proverb)