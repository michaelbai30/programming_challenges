import sys

def maxFourSquare(matrix):
    numRows = len(matrix)
    numCols = len(matrix[0])

    # we want virtually any value, no matter how small, to overwrite res first
    res = float('-inf')

    # sum of the current four square
    curSum = 0
     
    for r in range(numRows):
        for c in range(numCols):
            # ensures indices are in bounds
            if r+1 < numRows and c+1 < numCols:
                curSum = matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1]
                if curSum > res:
                    res = curSum
    return res

matrix = []
matrices = [] # contains a list of the matrices read in 

while True:
    n = sys.stdin.readline()
    if n == "0 0\n":
        break

    numRows, numCols = map(int, n.split(' '))

    # read numRow lines ahead
    for i in range(numRows):
       n = sys.stdin.readline()
       # from n, form a list of numbers, separated by a space, numCols amount of times
       elements = [int(element) for element in n.split(' ', numCols)]
       matrix.append(elements)

    # append the matrix to the list of matrices
    matrices.append(matrix.copy())
    matrix.clear()

for i, matrix in enumerate(matrices):
    print(f'{i+1}. Maximum four square is: {maxFourSquare(matrix)}')
