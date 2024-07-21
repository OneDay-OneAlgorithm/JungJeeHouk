import datetime

h, m = map(int, input().split())
dt = datetime.datetime(2023, 7, 21, h, m)
targetDt = dt + datetime.timedelta(minutes=-45)
print(targetDt.hour, targetDt.minute)