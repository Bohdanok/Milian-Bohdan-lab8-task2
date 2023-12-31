'''Check whether the board given is suitable for the puzzle game
Link to Github: https://github.com/Bohdanok/Milian-Bohdan-lab8-task2
'''
def validate_board(board:list)->bool:
    '''
    Checks for matche in the board and returns it's validity in bool type

    >>> validate_board([ "**** ****", "***1 ****", "**  3****", "* 4 1****", \
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board([ "**** ****", "***1 ****", "**  3****", "* 4 7****", \
"     9 5 ", " 6  83  *", "3   0  **", "  8  2***", "  2  ****"])
    True
    '''
    # Check colums
    for i in range(9):
        memory_list=[]
        for j in range(9):
            if board[j][i] !='*'and board[j][i] !=' ':
                memory_list.append(board[j][i])
                if board[j][i] in memory_list[:-1]:
                    return False
    # Check rows
    for i in board:
        memory_list=[]
        for j in i:
            if not j in ('*',' '):
                memory_list.append(j)
                if j in  memory_list[:-1]:
                    return False
    return check_color(board)
def check_color(board:str)->bool:
    '''
    Checks whether same elements are in same colors
    >>> check_color([ "****5****", "***1 ****", "**  3****", "* 4 7****", \
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> check_color([ "**** ****", "***1 ****", "**  3****", "* 4 7****", \
"     9 5 ", " 6  83  *", "3   0  **", "  8  2***", "  2  ****"])
    True
    '''
    # Check colors
    minus_colum=4
    minus_row=8
    plus_row=1
    for i in range(5):
        memory_list=[]
        for colum in range(5):
            # print(board[colum+minus_colum][i])
            if board[colum+minus_colum][i] !='*'and board[colum+minus_colum][i] !=' ':
                memory_list.append(board[colum+minus_colum][i])
                if board[colum+minus_colum][i] in memory_list[:-1]:
                    return False
        for row in range(4):
            # print (board[minus_row][row+plus_row])
            if  board[minus_row][row+plus_row] !='*'and board[minus_row][row+plus_row] !=' ':
                memory_list.append(board[minus_row][row+plus_row])
                if board[minus_row][row+plus_row] in memory_list[:-1]:
                    return False
        minus_colum-=1
        minus_row-=1
        plus_row+=1
    return True
if __name__=='__main__':
    import doctest
    print(doctest.testmod())
