def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while deliveries or pickups:
        delivery_load = 0
        pickup_load = 0
        distance = 0
        
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