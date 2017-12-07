board = [['1','2','3'], 
         ['4','5','6'],
         ['7','8','9']]

##draws board for tic-tac-toe
# Allows the game to run
def main():      
    """This ensures the game rund"""
    win = 0
    printBoard()
    Player_1(board, 3)
    
#Ensures that each square on the board to be updated
def setElem (elem, position, board, boardsize):     
    """Updates the position on the board"""
    for i in range (3):
        for j in range (3):
            print(board[i][j].format(board[i][j]))
            if (board[i][j] == position):
                print('position in board found')
                board[i][j] = elem
                
    print('board in setElem is {}'.format(board))
    return board

#Gives Player 1 "X's" and asks the player where the want to play    
def Player_1 (board,boardsize):            
    """Sets element for player 1 and defines win message"""
    elem = 'X'
    position = input("Where would you like to play?")
    board = setElem(elem, position, board, boardsize)
    drawBoard(board,boardsize)
    win = checkWin(board,boardsize)
    if (win==False):
        Player_2(board,boardsize)
    else:
        print('Congratulations Player 1! You win!') #Displays that Player 1 has won
        
#Gives Player 2 "O's" and asks the player where the want to play    
def Player_2 (board,boardsize):                     
    """Sets element for player 2and defines win message"""
    elem = 'O'
    position = input("Where would you like to play?")
    board = setElem(elem, position, board, boardsize)
    drawBoard(board,boardsize)
    win = checkWin(board,boardsize)
    if (win==False):
        Player_1(board,boardsize)
    else:
        print('Congratulations Player 2! You win!') #Displays that Player 2 has won
        
def printBoard():    
    """Defines how big the board will be"""
    boardsize = 3                                               #define board dimension
    board = defineBoard(boardsize)
    createBoardLabels(board, boardsize)
    drawBoard(board, boardsize)

def defineBoard(boardsize):
    """Makes the board"""
    board = [[""] * boardsize for i in range(boardsize)]#make the basic (non-drawable) version of theboard
    return board

def createBoardLabels(board, boardsize):                        #<lables the board>
    """Lables each square"""
    counter = 0
    for i in range(boardsize):
        for j in range(boardsize):
            counter +=1
            board[i][j] = counter
    return (board)

def print_divider (boardsize):                                  #<draws the lines on the board>
    """Prints lines between the squares"""
    print ('|'.join(['____' for x in range(boardsize)])) 

def print_blank (boardsize):
    """Prints blank squares"""
    print ('|'.join(['    ' for x in range(boardsize)]))        #<also draws lines on the board>

def print_labels(counter, board, boardsize):                    #<also draws lines on the board>
    """Prints lables on board"""
    row = ' | '.join(['%2s' % board[counter][x] for x in range(boardsize)])
    row = ' ' + row
    print(row)
   
def drawBoard(board, boardsize):                                #<prints blank spaces between the lines
    """Draws the board"""
    for i in range(boardsize):
        print_blank(boardsize)
        print_labels(i,board, boardsize)
        if (i == boardsize-1):
            print_blank(boardsize)
        else:
            print_divider(boardsize)          
            


#run the program
#This checks the first vertical column
def win1 (board):
    """Checks for a win"""
    win = True
    j = 0
    for i in range (2):
        if board [i][j] != board [i+1][j]:
            win = False
    return (win)

#This checks the second vertical column
def win2 (board):
    """Checks for a win"""
    win = True
    j = 1
    for i in range (2):
        if board [i][j] != board [i+1][j]:
            win = False
    return (win)

#This checks the third vertical column
def win3 (board):
    """Checks for a win"""
    win = True
    j = 2
    for i in range (2):
        if board [i][j] != board [i+1][j]:
            win = False
    return (win)


#This checks the first horizontal row
def win4 (board):
    """Checks for a win"""
    win = True
    i = 0
    for j in range (2):
        if board [i][j] != board [i][j+1]:
            win = False
    return (win)

#This checks the second horizontal row
def win5 (board):
    """Checks for a win"""
    win = True
    i = 1
    for j in range (2):
        if board [i][j] != board [i][j+1]:
            win = False
    return (win)

#This checks the third horizontal row
def win6 (board):
    """Checks for a win"""
    win = True
    i = 2
    for j in range (2):
        if board [i][j] != board [i][j+1]:
            win = False
    return (win)

#This checks the first diagonal row
def win7 (board):
    """Checks for a win"""
    win = True
    #j = 0
    for i in range (2):
        if board[i][i] != board[i+1][i+1]:
            win = False
       # j=j+1  
    return (win)
#This checks the second diagonal row
def win8 (board):
    """Checks for a win"""
    win = True
    j = 2
    for i in range (2):
        if board [i][j] != board [i+1][j-1]:
            win = False
        j=j-1      
    return (win)

def checkWin(board,boardsize):
    """Calls win functions"""
    if win1(board) or win2(board) or win3(board) or win4(board) or win5(board) or win6(board) or win7(board) or win8(board):
        #win = True
        print('True')
        return True
    else:
        print('False')
        return False

checkWin(board,3)
main()
