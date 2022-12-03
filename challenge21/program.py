import sys
import math
sys.setrecursionlimit(2000)

def prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# All carmichael numbers cannot be perfect squares
def perfect_square(num):
    sqr_root = int(math.sqrt(num))
    return num == sqr_root * sqr_root

# quick mod
def modexp(x, n, mod):
    if n == 0:
        return 1 % mod
    r = modexp(x, n / 2, mod)
    r = (r * r) % mod
    if n % 2:
        r = (r * x) % mod
    return r

def is_carmichael(num):
    x = 2
    if prime(num) or perfect_square(num):
        return False

    while x < num:
        if prime(num) and modexp(x, num, num) != x :
            return False
        x += 1

    return True

def main():
    cases = []
    for line in sys.stdin:
        cases.append(int(line.strip()))
    for case in cases:
        if is_carmichael(case) == True:
            print(f'The number {case} is a Carmichael number.')
        else:
            print(f'{case} is normal.')

if __name__ == '__main__':
    main()
