from typing import List

def merge(a: List[int], lo: int, mid: int, hi: int) -> None:
    tmp = a[mid:hi]
    ptr_1 = mid - 1
    ptr_2 = hi - mid - 1
    for i in range(hi-1,lo-1,-1):
        if ptr_1 < lo:
            a[i] = tmp[ptr_2]
            ptr_2 -= 1
        elif ptr_2 < 0:
            a[i] = a[ptr_1]
            ptr_1 -= 1
        elif a[ptr_1] < tmp[ptr_2]:
            a[i] = tmp[ptr_2]
            ptr_2 -= 1
        else:
            a[i] = a[ptr_1]
            ptr_1 -= 1
    return

def merge_sort(numbers: List[int]) -> None:
    if len(numbers) <= 1:
        return
    else:
        step = 1
        runs = [i for i in range(0,len(numbers),step)]
        while len(runs) > 1:
            for i in range(1,len(runs),2):
                if i+1 == len(runs):
                    merge(numbers,runs[i-1],runs[i],len(numbers))
                else:
                    merge(numbers,runs[i-1],runs[i],runs[i+1])
            step *= 2
            runs = [i for i in range(0,len(numbers),step)]
        return
    
def main() -> None:
    numbers1 = []
    print(numbers1)
    merge_sort(numbers1)
    print(numbers1)

    numbers2 = [1]
    print(numbers2)
    merge_sort(numbers2)
    print(numbers2)

    numbers3 = [1, 4, 3, 1, 7, 6, 2, 2, 5, 2]
    print(numbers3)
    merge_sort(numbers3)
    print(numbers3)

if __name__ == '__main__':
    main()