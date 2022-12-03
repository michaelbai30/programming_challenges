import sys

def least_perfect_squares(num):
    
    # initialize dynamic programming table
    table = [sys.maxsize] * (num + 1)
    table[0] = 0
    
    for target in range(1, num + 1):
        for source in range(1, target + 1):
            res = source ** 2
            # overshoot error
            # continue to next target
            if res - target > 0:
                break
            table[target] = min(table[target - res] + 1, table[target])
            
    # least num of perfect squares (solution)
    return table[num]

def main():
    cases = []
    for line in sys.stdin:
        cases.append(int(line.strip()))
    for case in cases:
        print(least_perfect_squares(case))

if __name__ == '__main__':
    main()