import sys

# from a given starting digit, list out all possible knight paths
number_paths = {
    0 : [4, 6],
    1 : [6, 8],
    2 : [7, 9],
    3 : [4, 8],
    4 : [0, 3, 9],
    5 : [],
    6 : [0, 1, 7],
    7 : [2, 6],
    8 : [1, 3],
    9 : [2, 4],
}

def knight_dialer(start, num_hops, combo):

    # base case: we've done num_hops hops
    if num_hops == 0:
        return [combo]
    
    res = []
    # for each digit in start's possible knight paths
    for next_digit in number_paths[start]:
        # call knight_dialer recursively, decrementing hops and appending the new digit to the current combo
        combos = knight_dialer(next_digit, num_hops - 1, combo + str(next_digit))
        res.extend(combos)
    return res

def main():
    test_cases = []
    for line in sys.stdin:
        start, num_hops = map(int, line.split())
        test_cases.append([start, num_hops])

    for i, test in enumerate(test_cases):
        if i != 0: # is there a better way to not print out a new line for the first case?
            print('')
        start, num_hops, combo = test[0],test[1] , str(test[0])
        combos = knight_dialer(start, num_hops - 1, combo)
        for combo in combos:
            print(combo)
        
    
if __name__ == '__main__':
    main()
   