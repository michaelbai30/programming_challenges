import sys
import math

def masked_bits(mask, bitstream):
    
    # string (from sys.stdin) -> int -> binary
    bin_mask = "{0:04b}".format(int(mask, 16))
    bin_bitstream = "{0:032b}".format(int(bitstream))

    # how many times a particular mask appears in each bitstream.
    count = 0

    # Ex: for bitstream len 8 and mask len 4,
    # the mask can fit 8 - 4 + 1 = 5 times into the size of the bitstream.
    for i in range(len(bin_bitstream) - len(bin_mask) + 1):
        # O(n) sliding window
        if bin_bitstream[i : i + len(bin_mask)] == bin_mask:
            count += 1
    return count

def main():
    list_of_cases = []
    for line in sys.stdin:
        list_of_cases.append([element for element in line.strip().split(' ')])
    
    for i, case in enumerate(list_of_cases):
        mask = case[0]
        bitstream = case[1]
        result = masked_bits(mask, bitstream)
        print(f'{i + 1}. {bitstream} contains 0x{mask} {result} times')

if __name__ == '__main__':
    main()

