
from datetime import datetime
import time

t1 = 1546300800
t2 = 1548892800
print(t1-t2)
# time tuple in utc time to timestamp
time_tuple_utc = (2018, 12, 31, 00, 00, 00, 0, 0, 0)
timestamp_utc = calendar.timegm(time_tuple_utc)
