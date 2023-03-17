def sort_r(matrix):
    for row in matrix:
        row_sum = sum(row)
        row.insert(0, row_sum)

    matrix.sort()
    for row in matrix:
        row.pop(0)

    return matrix

def display_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

matrix = []
rows = int(input())
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
sorted_matrix = sort_rows(matrix)
display_matrix(sorted_matrix)