import sys

def max_concurrent_events(intervals):
    
    # sorting works because determining number of concurrent events 
    # is actually commutative in the sense that the beginning and end
    # values of each INDIVIDUAL event does not matter. 

    # extract and sort beginning and end times for each event
    begin = []
    end = [] 
    for event in intervals:
        begin.append(event[0])
    for event in intervals:
        end.append(event[1])
    begin.sort()
    end.sort()

    num_concurrent_events = 0
    max_num_concurrent_events = 0
    i = 0
    j = 0

    # goes through E times where E is the number of events 
    while i < len(begin) and j < len(end):
        if begin[i] <= end[j]: # keep comparing beginning indexes with end indexes until beginning indexes are greater 
            num_concurrent_events += 1 # if this is the case, there is a new concurrent event
            # update final result if current num concurrent events beats the current max
            max_num_concurrent_events = max(num_concurrent_events, max_num_concurrent_events)
            i += 1
        
        else: # we decrement num_concurrent_events
            num_concurrent_events -= 1
            j += 1

    return max_num_concurrent_events

def main():
    
    intervals = []
    list_of_n_intervals = []
    for line in sys.stdin:
        num_events_to_read = line
        for i in range(int(num_events_to_read)):
            one_event = sys.stdin.readline() 
            event = [int(element) for element in one_event.strip().split(' ')] # one event parsed by ' ' into an interval list
            intervals.append(event.copy())
    
        list_of_n_intervals.append(intervals.copy())
        intervals.clear()
            
    for i, interval in enumerate(list_of_n_intervals):
        print(f'{i + 1}. Maximum number of concurrent events is {max_concurrent_events(interval)}')

if __name__ == '__main__':
    main()