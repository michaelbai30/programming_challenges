import sys

def search_rotated_array(nums, target):
    l = 0
    r = len(nums) - 1
        
    while l <= r:
        mid = (l + r) // 2

        # target found 
        if target == nums[mid]:
            return mid
            
        # mid is in the left sorted part of the array
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        # mid is in the right sorted part of the array
        else:
            if target > nums[r] or target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

    return None

def main():

    list_of_nums = []
    targets = []
    flag = 0

    # if flag is 0, read in rotated arrays of numbers sorted in ascending order
    for line in sys.stdin:
        if flag == 0:
            elements = line.strip().split(' ')
            list_of_nums.append([int(e) for e in elements])
            flag = 1
    
        # if flag is 1, read in the target values 
        elif flag == 1:
            element = line.strip()
            targets.append(int(element))
            flag = 0

    for i, nums in enumerate(list_of_nums):
        if search_rotated_array(nums, targets[i]) != None:
            print(f'{targets[i]} found at index {search_rotated_array(nums, targets[i])}')
        else:
            print(f'{targets[i]} was not found')

if __name__ == '__main__':
    main()
