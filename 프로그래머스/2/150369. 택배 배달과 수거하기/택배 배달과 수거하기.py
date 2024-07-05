# def solution(cap, n, deliveries, pickups):
#     deliveries = deliveries[::-1]
#     pickups = pickups[::-1]
#     answer = 0
    
#     d_sum = 0
#     p_sum = 0
    
#     for i in range(n):
#         d_sum += deliveries[i]
#         p_sum += pickups[i]
    
#     i = 0
#     while i < n:
#         while i < n and deliveries[i] == 0 and pickups[i] == 0:
#             i += 1
        
#         if i < n:
#             delivery_load = 0
#             pickup_load = 0
            
#             max_distance = n - i
            
#             for j in range(i, n):
#                 if delivery_load + deliveries[j] > cap:
#                     deliveries[j] -= (cap - delivery_load)
#                     delivery_load = cap
#                 else:
#                     delivery_load += deliveries[j]
#                     deliveries[j] = 0
                
#                 if pickup_load + pickups[j] > cap:
#                     pickups[j] -= (cap - pickup_load)
#                     pickup_load = cap
#                 else:
#                     pickup_load += pickups[j]
#                     pickups[j] = 0
                
#                 if delivery_load == cap and pickup_load == cap:
#                     break
            
#             answer += max_distance * 2
    
#     return answer



def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # 양쪽 끝에서부터 탐색
    while deliveries or pickups:
        delivery_load = 0
        pickup_load = 0
        distance = 0
        
        # 가장 먼 거리 계산
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        while pickups and pickups[-1] == 0:
            pickups.pop()
        
        distance = max(len(deliveries), len(pickups))

        while deliveries and delivery_load + deliveries[-1] <= cap:
            delivery_load += deliveries.pop()
        if deliveries and delivery_load < cap:
            deliveries[-1] -= (cap - delivery_load)

        while pickups and pickup_load + pickups[-1] <= cap:
            pickup_load += pickups.pop()
        if pickups and pickup_load < cap:
            pickups[-1] -= (cap - pickup_load)

        answer += distance * 2

    return answer