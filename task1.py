import heapq


def min_price(nums):
    if not nums:
        return 0

    heapq.heapify(nums)
    sum_cost = 0
    while len(list_lenghts) > 1:
        min_c1 = heapq.heappop(list_lenghts)
        min_c2 = heapq.heappop(list_lenghts)

        cost = min_c1 + min_c2
        sum_cost += cost

        heapq.heappush(nums, cost)
        print(nums)

    return sum_cost


list_lenghts = [4, 10, 3, 5, 1, 8]
print(min_price(list_lenghts))
