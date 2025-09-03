import heapq

def main() -> None:
    array = [15,9,1,17,11,25,36,19,100]
    array = [-item for item in array]
    print([-item for item in array])
    heapq.heapify(array)
    print([-item for item in array])

    heapq.heappush(array, -6)
    heapq.heappush(array, -12)
    print([-item for item in array])
    heapq.heappush(array, -13)
    heapq.heappush(array, -8)
    print([-item for item in array])
    heapq.heappush(array, -4)
    heapq.heappush(array, -5)
    print([-item for item in array])

    sorted_array = []
    sorted_array.append(heapq.heappop(array))
    print([-item for item in array], [-item for item in sorted_array])
    sorted_array.append(heapq.heappop(array))
    print([-item for item in array], [-item for item in sorted_array])
    sorted_array.append(heapq.heappop(array))
    print([-item for item in array], [-item for item in sorted_array])

    item = heapq.heappushpop(array, sorted_array[-1])
    print([-item for item in array], -item)
    item = heapq.heapreplace(array, sorted_array[-1])
    print([-item for item in array], -item)

if __name__ == '__main__':
    main()