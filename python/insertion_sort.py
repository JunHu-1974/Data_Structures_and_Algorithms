from typing import List
import bisect

def insertion_sort(numbers: List[int]) -> List[int]:
    if not numbers:
        return []
    elif len(numbers) == 1:
        return numbers[:]
    else:
        sorted_numbers = [numbers[0]]
        for i in range(1,len(numbers)):
            bisect.insort(sorted_numbers, numbers[i])
        return sorted_numbers
    
def main() -> None:
    numbers1 = []
    print(numbers1)
    print(insertion_sort(numbers1))

    numbers2 = [1]
    print(numbers2)
    print(insertion_sort(numbers2))

    numbers3 = [1, 4, 3, 1, 7, 6, 2, 2, 5, 2]
    print(numbers3)
    print(insertion_sort(numbers3))

if __name__ == '__main__':
    main()