Problem Statement: Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking for n-queens problem or a graph coloring problem
------------------------Program-----------------------------------------------

def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, 4, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col):
    if col >= 4:
        return True
    
    for i in range(4):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1):
                return True
            board[i][col] = 0
    
    return False

def solve_n_queens():
    board = [[0 for _ in range(4)] for _ in range(4)]
    
    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False
    
    print_board(board)
    return True

def print_board(board):
    for i in range(4):
        for j in range(4):
            print(board[i][j], end=" ")
        print()

solve_n_queens()

------------------Output-----------------
0 0 1 0 
1 0 0 0 
0 0 0 1 
0 1 0 0
