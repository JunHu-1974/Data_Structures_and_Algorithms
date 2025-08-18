from typing import List
import bisect

def insertion_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return
    else:
        for i in range(1,len(numbers)):
            tmp = numbers[i]
            j = i
            while j > 0 and numbers[j-1] > tmp:
                numbers[j] = numbers[j-1]
                j -= 1
            numbers[j] = tmp
        return
    
def main() -> None:
    numbers1 = []
    print(numbers1)
    insertion_sort(numbers1)
    print(numbers1)

    numbers2 = [1]
    print(numbers2)
    insertion_sort(numbers2)
    print(numbers2)

    numbers3 = [1, 4, 3, 1, 7, 6, 2, 2, 5, 2]
    print(numbers3)
    insertion_sort(numbers3)
    print(numbers3)

if __name__ == '__main__':
    main()