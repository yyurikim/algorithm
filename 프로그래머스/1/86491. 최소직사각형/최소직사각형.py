def solution(sizes):
    row_min = 0
    col_min = 0
    for size in sizes: 
        row_min = max(row_min, min(size))
        col_min = max(col_min, max(size))
        
    answer = row_min * col_min
    return answer

