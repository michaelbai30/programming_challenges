import sys

def triplets(nums):
    length = len(nums)
    triplet_match =[]
    res = []

    # brute force triplet loop to find all triplet matches
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                # if three elements sum to 0 and each index is exclusive
                if nums[i] + nums[j] + nums[k] == 0 and i != j and j != k and i != k:
                    triplet_match = sorted(([nums[i], nums[j], nums[k]])) # triplet must be sorted
                    if triplet_match not in res:
                        res.append(triplet_match)

    return res

def main():
    test_cases = []
    list_of_matches = []
    for line in sys.stdin:
        raw_test_case = line.split(' ')
        test_case = [int(x) for x in raw_test_case]
        # example input: -1 0 1 2 -1 -4
        # output: [[-1 , 0, 1 , 2, -1, -4]]
        test_cases.append(test_case) 
    
    for test_case in test_cases:
        list_of_matches.append(triplets(test_case)) # call triplets on each test case
    
    for res in list_of_matches:
        res.sort() # sort triplet matches  

    for i, res in enumerate(list_of_matches):
        if i != 0: # ensure there is a single blank line between outputs
            print('')
        for match in res:
            print(f'{match[0]} + {match[1]} + {match[2]}') 

if __name__ == '__main__':
    main()