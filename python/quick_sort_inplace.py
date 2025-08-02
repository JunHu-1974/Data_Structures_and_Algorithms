from typing import List

def quick_sort(numbers: List[int], lo: int, hi: int) -> None:
    if lo >= hi or lo < 0:
        return
    pivot = numbers[hi]
    pos = lo
    for i in range(lo, hi):
        if numbers[i] <= pivot:
            tmp = numbers[pos]
            numbers[pos] = numbers[i]
            numbers[i] = tmp
            pos += 1
    numbers[hi] = numbers[pos]
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