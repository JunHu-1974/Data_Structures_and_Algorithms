from typing import List

def quick_sort(numbers: List[int], lo: int, hi: int) -> None:
    if lo >= hi:
        return
    pivot = numbers[lo]
    pos = lo
    for i in range(lo+1, hi+1):
        if numbers[i] <= pivot:
            numbers[pos] = numbers[i]
            pos += 1
            numbers[i] = numbers[pos]
    numbers[pos] = pivot        
    quick_sort(numbers, lo, pos-1)
    quick_sort(numbers, pos+1, hi)
    
def main() -> None:
    numbers1 = []
    print(numbers1)
    quick_sort(numbers1, 0, len(numbers1)-1)
    print(numbers1)

    numbers2 = [1]
    print(numbers2)
    quick_sort(numbers2, 0, len(numbers2)-1)
    print(numbers2)

    numbers3 = [1, 4, 3, 1, 7, 6, 2, 2, 5, 2]
    print(numbers3)
    quick_sort(numbers3, 0, len(numbers3)-1)
    print(numbers3)

if __name__ == '__main__':
    main()