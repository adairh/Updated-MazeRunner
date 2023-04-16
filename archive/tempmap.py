filename = 'file.txt'

# read file contents into a list of lines
with open(filename, 'r') as f:
    lines = f.readlines()

# remove newline characters from each line
lines = [line.strip() for line in lines]

# determine the dimensions of the matrix
num_rows = len(lines)
num_cols = max(len(line) for line in lines)

# initialize the matrix with empty spaces
matrix = [[' ' for _ in range(num_cols)] for _ in range(num_rows)]

# fill in the matrix with characters from the file
string = ''
space_count = 0

for i in range(num_rows):
    for j in range(len(lines[i])):
        matrix[i][j] = lines[i][j]
        if lines[i][j] == 'x':
            string += '[' + str(i) + ',' + str(j) + '],'
        if lines[i][j] == ' ':
            space_count += 1

# print the matrix and space count for verification
print(string)
print("Space count:", space_count)
