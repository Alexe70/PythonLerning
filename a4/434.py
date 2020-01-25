from datetime import datetime
datetime_list = []
dt_list = ['2019-07-07T18:59:06', '2019-07-07T19:00:02', '2019-07-07T19:01:04']
for dt in dt_list:
    datetime_list.append(datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S'))

datetime_list = [
    datetime(2019, 7, 7, 18, 59, 6),
    datetime(2019, 7, 7, 19, 0, 2),
    datetime(2019, 7, 7, 19, 1, 4)
]

report_seconds = []

for dt in datetime_list:
    report_seconds.append(int(dt.second))

for sec in report_seconds:
    total_time += sec
# введите код здесь