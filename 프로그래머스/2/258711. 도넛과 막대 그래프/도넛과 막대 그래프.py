def solution(edges):
    answer = [0, 0, 0, 0]
    max_idx = 0
    for a, b in edges:
        max_idx = max(a, b, max_idx)
    
    nodes = [[0, 0] for _ in range(max_idx+1)]
    
    for f, t in edges:
        nodes[f][0] += 1
        nodes[t][1] += 1
    
    for idx in range(1, max_idx+1):
        if nodes[idx][0] >= 2 and nodes[idx][1] == 0:
            answer[0] = idx
        elif nodes[idx][0] == 0 and nodes[idx][1] >= 1:
            answer[2] += 1
        elif nodes[idx][0] == 2 and nodes[idx][1] >= 2:
            answer[3] += 1
    answer[1] = nodes[answer[0]][0] - sum(answer[2:])
    
    return answer