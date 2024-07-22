import datetime

h, m = map(int, input().split())
duration = int(input())
dt = datetime.datetime(2023, 7, 21, h, m)
targetDt = dt + datetime.timedelta(minutes=duration)
print(targetDt.hour, targetDt.minute)