import sys

input = sys.stdin.readline

N = int(input())

lst = [input().strip() for _ in range(N)]

cnt = 0

for word in lst:
    word_dict = {}
    flag = 1
    for i in range(len(word)):
        if i == 0:
            word_dict[word[i]] = 1
        else:
            if word[i-1] != word[i] and (word[i] in word_dict.keys()):
                flag = 0
                break
            else:
                if word[i] in word_dict.keys():
                    word_dict[word[i]] += 1
                else:
                    word_dict[word[i]] = 1
    cnt += flag


print(cnt)