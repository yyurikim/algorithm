for test_case in range(1, 11):
    tc = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    current_col = lst[99].index(2)
    current_row = 99

    while current_row > 0:
        if current_col > 0 and lst[current_row][current_col-1] == 1:
            if current_col < 99 and lst[current_row][current_col+1] == 0:
                while current_col - 1 >= 0 and lst[current_row][current_col - 1] == 1:
                    current_col = current_col - 1
                current_row = current_row - 1
            elif current_col == 99:
                while current_col - 1 >= 0 and lst[current_row][current_col - 1] == 1:
                    current_col = current_col - 1
                current_row = current_row - 1

        elif current_col < 99 and lst[current_row][current_col+1] == 1:
            if current_col > 0 and lst[current_row][current_col-1] == 0:
                while current_col + 1 <= 99 and lst[current_row][current_col + 1] == 1:
                    current_col = current_col + 1
                current_row = current_row - 1
            elif current_col == 0:
                while current_col + 1 <= 99 and lst[current_row][current_col + 1] == 1:
                    current_col = current_col + 1
                current_row = current_row - 1

        else:
            current_row = current_row - 1

    print(f'#{test_case} {current_col}')