def main() -> None:
    hash_set = set()
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

    print(hash_set)
    print('123-6574 has hash code:', hash('123-6574'))
    print('123-6574 is in the set:', '123-6574' in hash_set)
    hash_set.remove('123-6574')
    print('123-6574 has hash code:', hash('123-6574'))
    print('123-6574 is in the set:', '123-6574' in hash_set)

if __name__ == '__main__':
    main()