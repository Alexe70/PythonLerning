
import json
import collections

c = collections.Counter()

with open('file.json', 'rb') as infile:
    data = json.load(infile)
data_list = data['events_data']

clients = []
for item in data_list:
    client_id = item['client_id']
    category = item['category']
    if category == 'report':
        clients.append(client_id)
for cl in clients:
    c[cl] += 1

print(c)