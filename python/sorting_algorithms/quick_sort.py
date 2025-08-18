from typing import List

def quick_sort(numbers: List[int]) -> List[int]:
    if not numbers:
        return []
    elif len(numbers) == 1:
        return numbers[:]
    else:
        pivot = numbers[0]
        left = [n for n in numbers[1:] if n <= pivot]
        right = [n for n in numbers[1:] if n > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)
    
def main() -> None:
    numbers1 = []
    print(numbers1)
    print(quick_sort(numbers1))

    numbers2 = [1]
    print(numbers2)
    print(quick_sort(numbers2))

    numbers3 = [1, 4, 3, 1, 7, 6, 2, 2, 5, 2]
    print(numbers3)
    print(quick_sort(numbers3))

if __name__ == '__main__':
    main()