import heapq

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h,value) ## h라는 리스트에 vaule 값을 넣는다 ##최대힙은 데이터의 부호를 변경해서 집어넣으면 된다
        ##다시 꺼낼때 부호 -붙인다.

    for i in range(len(h)):
        result.append(heapq.heappush())
        

    return result

result = heapsort[1,3,5,7,9,11]

print(result)


    