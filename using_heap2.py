import heapq


def heapsort(iterable):

    q = []
    list_a =[]
    for data in iterable:
        heapq.heappush(q,data)

    for i in range(len(q)):
        list_a.append(heapq.heappop(q))
    
    return list_a