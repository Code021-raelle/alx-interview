#!/usr/bin/python3
"""
Pascal's triangle
"""
def pascal_triangle(n):
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        row = [1] # start each row with a 1
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1) # end each row with a 1
        triangle.append(row)

    return triangle
