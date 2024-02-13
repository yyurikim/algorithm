lst = [list(input()) for _ in range(5)]
max_len = 0
for k in lst:
    if len(k) > max_len:
        max_len = len(k)

result = ''

for i in range(max_len):
    for j in range(5):
        if 0 <= i < len(lst[j]):
            result += lst[j][i]

print(result)
