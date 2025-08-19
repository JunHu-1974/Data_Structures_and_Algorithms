class SimpleHashMap(object):
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for i in range(size)]
    
    def hash_function(self, key):
        return sum(ord(char) for char in key)

    def print(self):
        for index, bucket in enumerate(self.buckets):
            print('Bucket[{}]: {}'.format(index, bucket))

    def put(self, key, value):
        index = self.hash_function(key) % self.size
        bucket = self.buckets[index]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return
        bucket.append((key,value))

    def get(self, key):
        index = self.hash_function(key) % self.size
        bucket = self.buckets[index]
        for k,v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self.hash_function(key) % self.size
        bucket = self.buckets[index]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket.remove((k,v))
                return True
        return False

def main() -> None:
    hash_map = SimpleHashMap(size=10)
    hash_map.put('123-4567', 'Charlotte')
    hash_map.put('123-4568', 'Thomas')
    hash_map.put('123-4569', 'Jens')
    hash_map.put('123-4570', 'Peter')
    hash_map.put('123-4571', 'Lisa')
    hash_map.put('123-4573', 'Michaela')
    hash_map.put('123-4575', 'Peter')
    hash_map.put('123-4576', 'Bob')
    hash_map.put('123-4672', 'Adele')
    hash_map.put('123-6574', 'Bob')

    hash_map.print()
    print('123-6574 has hash code:', hash_map.hash_function('123-6574'))
    print('Value associated with key 123-6574:', hash_map.get('123-6574'))
    hash_map.put('123-6574', 'James')
    print('123-6574 has hash code:', hash_map.hash_function('123-6574'))
    print('Value associated with key 123-6574:', hash_map.get('123-6574'))
    hash_map.remove('123-6574')
    hash_map.print()
    print('Value associated with key 123-6574:', hash_map.get('123-6574'))

if __name__ == '__main__':
    main()