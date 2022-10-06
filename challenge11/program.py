import sys

def min_transactions(value):
    cache = {}
   
   # base cases
    cache[1] = 1
    cache[2] = 2
   
   # prepopulate table
    for i in range(3, value + 1):
        cache[i] = 1

    for i in range(1, value + 1):
        if i < 2:
            continue
       # if value of fortnite card is even, we can get to it through doubling half that value stored in the cache
        if i % 2 == 0:
            cache[i] = cache[i // 2] + 1 
       # else, we must get to it by adding one to the value to the left
        else:
            cache[i] = cache[i - 1] + 1   
    # return the last value in the table (we build up to that value)
    return cache[value]

def main():
    cases = []
    for line in sys.stdin:
        cases.append(int(line.strip()))
    for i, case in enumerate(cases):
        print(f'{i + 1}. Minimum number of doge transactions: {min_transactions(case)}')
    
if __name__ == '__main__':
    main()
