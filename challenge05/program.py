import sys

def get_collatz_cycle_length(num, collatz_cyc_len_dict):
    # special case: if num is already 1, just return 1
    if num == 1:
        return 1

    # if we have not yet stored the num's cycle len
    if num not in collatz_cyc_len_dict:
        if num % 2 == 1:
            # recursive call (3n + 1)
            cyc_len = get_collatz_cycle_length(3*num + 1, collatz_cyc_len_dict)
            collatz_cyc_len_dict[num] = cyc_len + 1
            return collatz_cyc_len_dict[num]
        else:
            # recursive call (n // 2)
            cyc_len = get_collatz_cycle_length(num//2, collatz_cyc_len_dict)
            collatz_cyc_len_dict[num] = cyc_len + 1
            return collatz_cyc_len_dict[num]
            
    else:
        return collatz_cyc_len_dict[num]

# find the largest cycle length from sequence begin to end
def get_max_cycle_len(begin, end, collatz_cyc_len_dict):
    max_cycle_len = 0
    while begin <= end:
        cycle_len = get_collatz_cycle_length(begin, collatz_cyc_len_dict)
        # if curr cycle_len beats max_cycle_len, update max
        max_cycle_len = max(cycle_len, max_cycle_len)
        begin+= 1

    # get the number who has the largest cycle len
    # given a value, get the key from a dictionary 
    for key, value in collatz_cyc_len_dict.items():
        if value == max_cycle_len:
            which_term = key
            return ([which_term,max_cycle_len])

store_memo = {}
num_arr = []
for line in sys.stdin:
    elements=line.split()
    begin = int(elements[0])
    end = int(elements[1])
    num_arr.append([begin, end])

for intervals in num_arr:
    if intervals[0] > intervals[1]:
        # results[0] = num with max cyc len
        # results[1] = the max cycle len
        results = get_max_cycle_len(intervals[1], intervals[0], store_memo)
    else:
       results = get_max_cycle_len(intervals[0], intervals[1], store_memo) 
    
    print(f"{intervals[0]} {intervals[1]} {results[0]} {results[1]}") 
    store_memo.clear()

