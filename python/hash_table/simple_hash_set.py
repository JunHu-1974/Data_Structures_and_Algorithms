class SimpleHashSet(object):
    def __init__(self, size: int = 100):
        self.size = size
        self.buckets = [[] for i in range(size)]
    
    def hash_function(self, key: str) -> int:
        return sum(ord(char) for char in key)

    def print(self) -> None:
        for index, bucket in enumerate(self.buckets):
            print('Bucket[{}]: {}'.format(index, bucket))

    def add(self, key: str) -> bool:
        index = self.hash_function(key) % self.size
        bucket = self.buckets[index]
        if not key in bucket:
            bucket.append(key)
            return True
        else:
            return False

    def remove(self, key: str) -> bool:
        index = self.hash_function(key) % self.size
        bucket = self.buckets[index]
        if key in bucket:
            bucket.remove(key)
            return True
        else:
            return False

    def contains(self, key: str) -> bool:
        index = self.hash_function(key) % self.size
        bucket = self.buckets[index]
        return key in bucket

def main() -> None:
    hash_set = SimpleHashSet(size=10)
    hash_set.add('123-4567')
    hash_set.add('123-4568')
    hash_set.add('123-4569')
    hash_set.add('123-4570')
    hash_set.add('123-4571')
    hash_set.add('123-4573')
    hash_set.add('123-4575')
    hash_set.add('123-4576')
    hash_set.add('123-4672')
    hash_set.add('123-6574')

    hash_set.print()
    print('123-6574 has hash code:', hash_set.hash_function('123-6574'))
    print('123-6574 is in the set:', hash_set.contains('123-6574'))
    hash_set.remove('123-6574')
    print('123-6574 has hash code:', hash_set.hash_function('123-6574'))
    print('123-6574 is in the set:', hash_set.contains('123-6574'))

if __name__ == '__main__':
    main()