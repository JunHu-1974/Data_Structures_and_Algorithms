from typing import Any

class SimplePriorityQueue(object):
    def __init__(self, array: list[Any], min_priority: bool = True):
        self.queue = array
        self.size = len(array)
        self.priority = min_priority
        if self.priority:
            self.queue.sort()
        else:
            self.queue.sort(reverse=True)

    def push(self, item: Any) -> None:
        pos = 0
        if self.priority:
            while pos < self.size:
                if self.queue[pos] > item:
                    break
                pos += 1
        else:
            while pos < self.size:
                if self.queue[pos] < item:
                    break
                pos += 1
        self.size += 1
        self.queue.insert(pos, item)

    def pop(self) -> Any:
        if not self.queue:
            return None
        else:
            self.size -= 1
            head = self.queue.pop(0)
            return head

    def replace(self, item: Any) -> Any:
        head = self.pop()
        self.push(item)
        return head

    def push_pop(self, item: Any) -> Any:
        if self.priority and item > self.queue[0]:
            return self.replace(item)
        elif not self.priority and item < self.queue[0]:
            return self.replace(item)
        else:
            return item

def main() -> None:
    array = [15,9,1,17,11,25,36,19,100]
    print(array)
    heap = SimplePriorityQueue(array, False)
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