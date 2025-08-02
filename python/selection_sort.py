from typing import List

def selection_sort(numbers: List[int]) -> List[int]:
    if not numbers:
        return []
    elif len(numbers) == 1:
        return numbers[:]
    else:
        unsorted_numbers = numbers[:]
        sorted_numbers = []
        while len(unsorted_numbers) > 0:
            m = min(unsorted_numbers)
            sorted_numbers.append(m)
            unsorted_numbers.remove(m)
        return sorted_numbers
    
def main() -> None:
    numbers1 = []
    print(numbers1)
    print(selection_sort(numbers1))

    numbers2 = [1]
    print(numbers2)
    print(selection_sort(numbers2))

    numbers3 = [1, 4, 3, 1, 7, 6, 2, 2, 5, 2]
    print(numbers3)
    print(selection_sort(numbers3))

if __name__ == '__main__':
    main()