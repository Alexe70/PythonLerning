emails_list = ['vasya@mail.ru',
                'akakiy@yandex.ru',
                'spyderman@yandex.ru',
                'XFiles@gmail.com',
                'hello@mail.ru',
                'noname@gmail.com',
                'DonaldTrump@mail.ru',
                'a768#af@yandex.ru',
                'Ivan_Ivanovich@yandex.ru',
                'thebestmail@yandex.ru']
emails_dict1=[]
for line in emails_list:
    info = line.split('@')
    if info[-1] in emails_dict1:
        continue
    else:
        emails_dict1.append(info[-1])
c=0
emails_dict_c=[]
for info in emails_dict1:
    for line in emails_list:
        if info == line.split('@')[-1]:
            c+=1
    emails_dict_c.append(c)
    c=0
emails_dict=dict.fromkeys(emails_dict1,emails_dict_c)
print (emails_dict)