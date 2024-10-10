def solution(answers):
    answer = []
    a_pick = [1, 2, 3, 4, 5]
    b_pick = [2, 1, 2, 3, 2, 4, 2, 5]
    c_pick = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    ans_cnt = {1: 0, 2: 0, 3: 0}
    
    for i in range(len(answers)):
        if answers[i] == a_pick[i%5]:
            ans_cnt[1] += 1
        if answers[i] == b_pick[i%8]:
            ans_cnt[2] += 1
        if answers[i] == c_pick[i%10]:
            ans_cnt[3] += 1
    
    max_cnt = max(ans_cnt.values())
    
    for key, val in ans_cnt.items():
        if val == max_cnt:
            answer.append(key)
        
    return answer