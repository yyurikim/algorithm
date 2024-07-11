import sys

input = sys.stdin.readline

T = int(input())

original_word = input().rstrip()

cnt = 0

for _ in range(T-1):
    compare_word = input().rstrip()
    new_comp_word = compare_word
    for alp in original_word:
        new_comp_word = new_comp_word.replace(alp, '', 1)
    if len(new_comp_word) >= 2:
        continue
    else:
        new_ori_word = original_word
        for alp in compare_word:
            new_ori_word = new_ori_word.replace(alp,'', 1)
        if len(new_ori_word) <= 1:
            cnt += 1

print(cnt)