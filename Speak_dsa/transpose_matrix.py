# Given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:

# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]


# Brute force - nested for-loop
def transpose(matrix):
    num_rows = len(matrix[0])
    num_cols = len(matrix)
    trans_matrix = []
    for r in range(num_rows):
        row = []
        for c in range(num_cols):
            row.append(matrix[c][r])
        trans_matrix.append(row)
    return trans_matrix

# m1 = [[1,2,3],[4,5,6]]
# # Output: [[1,4],[2,5],[3,6]]
# test1 = transpose(m1)
# print(test1)

# Runtime: 78 ms, faster than 56.31% of Python online submissions for Transpose Matrix.
# Memory Usage: 14.4 MB, less than 11.76% of Python online submissions for Transpose Matrix.

def transposeFast(matrix):
    trans_tuples = list(zip(*matrix))
    trans_matrix = [list(t) for t in trans_tuples]
    return trans_matrix

# Runtime: 55 ms, faster than 91.69% of Python online submissions for Transpose Matrix.
# Memory Usage: 14.5 MB, less than 6.54% of Python online submissions for Transpose Matrix.

m2 = [[1,2,3],[4,5,6]]
test2 = transposeFast(m2)
print(test2)