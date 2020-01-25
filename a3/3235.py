name = 'Севастиан'
consonant = 'свтн'
vowal = 'еаи'
for litter in name:
    if litter.lower() in consonant:
        print('{} - согласная буква'.format(litter))
    if litter.lower() in vowal:
        print('{} - гласная буква'.format(litter))