total = int(input())
n = int(input())
summary = 0
for i in range(n):
    p, m = map(int, input().split())
    summary += p * m
if summary == total:
    print('Yes')
else:
    print('No')