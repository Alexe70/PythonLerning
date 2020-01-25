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
domainList = []
unicDomainList = []

emails_dict = {}
index = 0
flag = True

for domain in emails_list:
    domainList.append(domain[(domain.find('@')+1):])
for domain in domainList:
    for unicDomain in unicDomainList:
        if domain == unicDomain:
            flag = False
            break
        else:
            flag = True
    if flag:
        unicDomainList.append(domain)
for domainCount in unicDomainList:
    count = domainList.count(domainCount)
    emails_dict[domainCount] = count
print(emails_dict)
