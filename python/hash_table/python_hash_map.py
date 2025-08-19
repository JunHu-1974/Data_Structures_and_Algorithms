def main() -> None:
    hash_map = dict()
    hash_map['123-4567'] = 'Charlotte'
    hash_map['123-4568'] = 'Thomas'
    hash_map['123-4569'] = 'Jens'
    hash_map['123-4570'] = 'Peter'
    hash_map['123-4571'] = 'Lisa'
    hash_map['123-4573'] = 'Michaela'
    hash_map['123-4575'] = 'Peter'
    hash_map['123-4576'] = 'Bob'
    hash_map['123-4672'] = 'Adele'
    hash_map['123-6574'] = 'Bob'

    print(hash_map)
    print('123-6574 has hash code:', hash('123-6574'))
    print('Value associated with key 123-6574:', hash_map['123-6574'])
    hash_map['123-6574'] = 'James'
    print('123-6574 has hash code:', hash('123-6574'))
    print('Value associated with key 123-6574:', hash_map['123-6574'])
    hash_map.pop('123-6574')
    print(hash_map)
    print('Value associated with key 123-6574:', hash_map.pop('123-6574', None))
    
if __name__ == '__main__':
    main()