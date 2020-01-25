from random import random

user_db = [{'orders': 12}, {'orders': 30}, {'orders': 45}]

# перепишите эту часть
def avg_orders(user_db):
  order_sum = sum([user['orders'] for user in user_db])
  orders_per_user = order_sum/len(user_db)
  return orders_per_user

res = avg_orders(user_db)
#print(res)


def get_euro_rate():
    rate = 0 
    while(rate < 65 or rate > 85):
        rate = int(random()*100)
    return rate
i = 1
while (i<100):
    print(get_euro_rate())
    i+=1