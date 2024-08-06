N, M = map(int, input().split())
buket = list(range(1, N+1))
for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    buket[i:j+1] = buket[i:j+1][::-1]
print(" ".join(map(str, buket)))