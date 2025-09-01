from typing import List

def selection_sort(numbers: List[int]) -> None:
    if len(numbers) <= 1:
        return
    else:
        for i in range(len(numbers)-1):
            j = i
            for k in range(i+1,len(numbers)):
                if numbers[k] < numbers[j]:
                    j = k
            if j > i:
                tmp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = tmp
        return
    
def main() -> None:
    numbers1 = []
    print(numbers1)
    selection_sort(numbers1)
    print(numbers1)

    numbers2 = [1]
    print(numbers2)
    selection_sort(numbers2)
    print(numbers2)

    numbers3 = [1, 4, 3, 1, 7, 6, 2, 2, 5, 2]
    print(numbers3)
    selection_sort(numbers3)
    print(numbers3)

if __name__ == '__main__':
    main()