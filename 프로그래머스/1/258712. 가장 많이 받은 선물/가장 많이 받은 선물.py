def solution(friends, gifts):
    # 딕셔너리를 활용하여 친구들 각각에 인덱스를 부여 - 행렬 만들기 위해
    friends_dict = {}
    for i in range(len(friends)):
        friends_dict[friends[i]] = i

    # lst : 선물 주고받은 횟수를 기록하는 이차원 리스트
    lst = [[0] * len(friends) for _ in range(len(friends))]

    for i in range(len(gifts)):
        a, b = gifts[i].split()
        lst[friends_dict[a]][friends_dict[b]] += 1

    # 선물 지수 계산을 위해 lst_z 리스트 생성
    lst_z = list(zip(*lst))

    # 선물 지수 : gift_idx
    gift_idx = []

    for i in range(len(friends)):
        gift_idx.append(sum(lst[i]) - sum(lst_z[i]))

    # 다음 달에 받을 선물 개수 : how_many_gifts
    how_many_gifts = [0] * len(friends)
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i != j:
                give_gift = lst[i][j]
                get_gift = lst[j][i]
                if give_gift != get_gift:
                    if give_gift > get_gift:
                        how_many_gifts[i] += 1
                    elif give_gift < get_gift:
                        how_many_gifts[j] += 1
                elif give_gift == get_gift:
                    if gift_idx[i] > gift_idx[j]:
                        how_many_gifts[i] += 1
                    elif gift_idx[i] < gift_idx[j]:
                        how_many_gifts[j] += 1

    return max(how_many_gifts)//2
