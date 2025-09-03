from typing import Any

class SimpleBinaryHeap(object):
    def __init__(self, array: list[Any], min_priority: bool = True):
        self.array = array
        self.size = len(array)
        self.priority = min_priority
        if self.priority:
            for i in range(self.size//2,-1,-1):
                self.sift_down_min(i)
        else:
            for i in range(self.size//2,-1,-1):
                self.sift_down_max(i)

    def sift_down_min(self, pos: int) -> None:
        left = 2 * pos + 1
        right = 2 * pos + 2
        smallest = pos
        if left < self.size and self.array[left] < self.array[smallest]:
            smallest = left
        if right < self.size and self.array[right] < self.array[smallest]:
            smallest = right
        if smallest != pos:
            self.array[smallest], self.array[pos] = self.array[pos], self.array[smallest]
            self.sift_down_min(smallest)

    def sift_down_max(self, pos: int) -> None:
        left = 2 * pos + 1
        right = 2 * pos + 2
        largest = pos
        if left < self.size and self.array[left] > self.array[largest]:
            largest = left
        if right < self.size and self.array[right] > self.array[largest]:
            largest = right
        if largest != pos:
            self.array[largest], self.array[pos] = self.array[pos], self.array[largest]
            self.sift_down_max(largest)

    def sift_up(self, pos: int) -> None:
        item = self.array[pos]
        curr = pos
        parent = 0
        if self.priority:
            while curr > 0 and parent >= 0:
                parent = (curr - 1) // 2
                if item < self.array[parent]:
                    self.array[curr] = self.array[parent]
                    curr = parent
                else:
                    parent = -1
        else:
            while curr > 0 and parent >= 0:
                parent = (curr - 1) // 2
                if item > self.array[parent]:
                    self.array[curr] = self.array[parent]
                    curr = parent
                else:
                    parent = -1
        self.array[curr] = item

    def push(self, item: Any) -> None:
        self.size += 1
        self.array.append(item)
        self.sift_up(self.size-1)

    def pop(self) -> Any:
        if not self.array:
            return None
        elif self.size == 1:
            self.size = 0
            return self.array.pop()
        else:
            item = self.array[0]
            self.array[0] = self.array[-1]
            self.size -= 1
            self.array.pop()
            if self.priority:
                self.sift_down_min(0)
            else:
                self.sift_down_max(0)
            return item

    def replace(self, item: Any) -> Any:
        self.array[0], item = item, self.array[0]
        if self.priority:
            self.sift_down_min(0)
        else:
            self.sift_down_max(0)
        return item

    def push_pop(self, item: Any) -> Any:
        if self.priority and item > self.array[0]:
            return self.replace(item)
        elif not self.priority and item < self.array[0]:
            return self.replace(item)
        else:
            return item

def main() -> None:
    array = [15,9,1,17,11,25,36,19,100]
    print(array)
    heap = SimpleBinaryHeap(array, False)
    print(array)

    heap.push(6)
    heap.push(12)
    print(array)
    heap.push(13)
    heap.push(8)
    print(array)
    heap.push(4)
    heap.push(5)
    print(array)

    sorted_array = []
    sorted_array.append(heap.pop())
    print(array, sorted_array)
    sorted_array.append(heap.pop())
    print(array, sorted_array)
    sorted_array.append(heap.pop())
    print(array, sorted_array)

    item = heap.push_pop(sorted_array[-1])
    print(array, item)
    item = heap.replace(sorted_array[-1])
    print(array, item)

if __name__ == '__main__':
    main()