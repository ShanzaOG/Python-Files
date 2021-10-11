import time


board = [
    [0, 0, 0, 9, 0, 0, 5, 0, 0],
    [3, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 8],
    [0, 4, 0, 0, 0, 2, 0, 0, 5],
    [0, 0, 3, 0, 9, 0, 1, 0, 0],
    [4, 0, 0, 6, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 3, 4, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 2, 9, 0]
]


def solve(bo): # This function checks if there is an empty space in both row and column and the small box.
    find = find_empty(bo) # This line finds
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, n, pos):  # Takes three arguments board, number and position
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == n and pos[1] != i:
            return False
    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == n and pos[0] != i:
            return False

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == n and (i, j) != pos:
                return False

    return True


def board_grid(bo):
    for i in range  (len(bo)) :
        if i % 3 == 0 and i != 0 :
          print ("_ _ _ _ _ _ _ _ _ _ _ ")

        for j in range (len(bo[0])) :
             if j % 3 == 0 and j != 0:
              print ("|", end=" ")
             if j == 8:
              print(bo [i] [j])
             else:
              print(str (bo[i] [j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i] [j] == 0:
                return(i,j)  #returns row, column
    return None


start = time.time()

board_grid(board)
print('-----------------------------')
solve(board)
print('SOLUTION')
board_grid(board)
stop = time.time()

print(stop - start)
