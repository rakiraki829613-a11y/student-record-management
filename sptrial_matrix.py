def spiral(matrix):
    result = []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while left <= right and top <= bottom:

        # Top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(spiral(matrix))h