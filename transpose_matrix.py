def transpose(matrix):
    c = 0
    for i in range(0,len(matrix_value[0])):
        empty = list()
        for r in matrix:
            empty.append(r[c])
        c+=1
        column.append(empty)

column = list()

# Change this
matrix_value =   [[ 1, 4, 2, 5, 3, 2, 5 ],
                 [ 5, 1, 6, 3, 6, 7, 9 ],
                 [ 6, 3, 3, 2, 7, 6, 2 ],
                 [ 5, 1, 6, 3, 6, 7, 9 ],
                 [ 4, 41, 4, 54, 4, 1, 0 ],
                 [ 5, 1, 6, 3, 6, 7, 9],
                 [ 25, 5, 75, 75, 5, 2, 5 ],
                 [ 6, 2, 1, 61, 1, 42, 9]]

try:
    transpose(matrix_value)         # Transpose function
except IndexError as err:
    print(f"IndexError {err}")
    exit()

for k in matrix_value:
    print(k)

print("\n")


for j in column:
    print(j)