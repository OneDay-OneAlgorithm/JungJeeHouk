N = int(input())
words_set = set([])
for i in range(N):
    words_set.add(input())

words = list(words_set)
words.sort()
words.sort(key=len)
for word in words:
    print(word)