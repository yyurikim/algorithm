import sys
input = sys.stdin.readline

word = input().strip().upper()


word_cnt = {}
max_amt = 0
max_alps = []
for alp in word:
    if alp in word_cnt:
        word_cnt[alp] += 1
    else:
        word_cnt[alp] = 1

max_amt = max(word_cnt.values())


for a,c in word_cnt.items():
    if c == max_amt:
        max_alps.append(a)


if len(max_alps) >= 2:
    print('?')
else:
    print(max_alps[0])