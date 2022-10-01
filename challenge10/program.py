import sys

def min_candies(students):
    num_students = len(students)

    # each student must get at least one candy
    res = [1] * num_students

    # first pass:
    # ensure that students with a higher rating get more candy than their left neighbor
    for i in range(num_students - 1):
        if students[i + 1] > students[i]:
            # add +1 candy so that right neighbor has more.
            # if res[i + 1] already has more than left neighbor, the max will return that value
            res[i + 1] = max(res[i + 1], res[i] + 1)

    # second pass: iterate backwards
    for i in range(num_students - 2, -1, -1):
        if students[i + 1] < students[i]:
            res[i] = max(res[i], res[i + 1] + 1)

    return sum(res)

def main():
    list_of_cases = []

    for line in sys.stdin:
        list_of_cases.append([int(e) for e in line.strip().split(' ')])

    for i, case in enumerate(list_of_cases):
        print(f'{i + 1}. You need {min_candies(case)} candies.')
        
if __name__  == '__main__':
    main()

