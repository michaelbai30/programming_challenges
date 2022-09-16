import sys

def distinct_fruit(fruits):

    hash_table = {}
    curr_len = 0
    max_len = 0
    max_seq = ''

    # starting position of substring containing the max len seq of distinct fruit
    start = -1 # default = -1

    for i, fruit in enumerate(fruits):
        # if already hashed and new start index is farther along than curr start
        if fruit in hash_table and hash_table[fruit] > start:
            # update start
            start = hash_table[fruit]
        
        # add to hash, even if already hashed
        hash_table[fruit] = i
        curr_len = i - start 
        if curr_len > max_len: # new max_seq
            max_seq = fruits[start + 1 : i + 1]
        max_len = max(max_len, curr_len)

    return max_len, max_seq

def main():
    # list of test cases
    fruits_list = []

    for line in sys.stdin:
        fruits = line.strip().split(' ')
        fruits_list.append(fruits)
    
    for fruits in fruits_list:
        print(f'{distinct_fruit(fruits)[0]}: {", ".join(distinct_fruit(fruits)[1])}')

if __name__ == '__main__':
    main()