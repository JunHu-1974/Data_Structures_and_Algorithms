from typing import List

def merge(a: List[int], b: List[int]) -> List[int]:
    ptr_a = 0
    ptr_b = 0
    merged = []
    while ptr_a < len(a) or ptr_b < len(b):
        if ptr_a == len(a):
            merged.append(b[ptr_b])
            ptr_b += 1
        elif ptr_b == len(b):
            merged.append(a[ptr_a])
            ptr_a += 1
        elif a[ptr_a] > b[ptr_b]:
            merged.append(b[ptr_b])
            ptr_b += 1
        else:
            merged.append(a[ptr_a])
            ptr_a += 1
    return merged

def merge_sort(numbers: List[int]) -> List[int]:
    if not numbers:
        return []
    elif len(numbers) == 1:
        return numbers[:]
    else:
        runs = [numbers[i:i+1] for i in range(len(numbers))]
        i = 0
        while i < len(runs)-1:
            first = runs[i]
            second = runs[i+1]
            runs.append(merge(first, second))
            i += 2
        return runs[i]
    
def main() -> None:
    numbers1 = []
    print(numbers1)
    print(merge_sort(numbers1))

    numbers2 = [1]
    print(numbers2)
    print(merge_sort(numbers2))

    numbers3 = [1, 4, 3, 1, 7, 6, 2, 2, 5, 2]
    print(numbers3)
    print(merge_sort(numbers3))

if __name__ == '__main__':
    main()