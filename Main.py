import random

# Global variables
grd = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
gameover = False
turn_count = 0
draw = False

# init_grid()
'''Initialize grid values with '[ ]'''
def init_grid(a_grid):
    for row in a_grid:
        for col in range(0, len(row)):
            row[col] = "[ ]"

'''Function that prints the grid'''
def print_grid(a_grid):
    print("   0   1   2")
    for i, row in enumerate(grd):
        print(i),
        for col in range(0,len(row)):
            print(row[col]),
        print("\n")

# ask_int
'''Checks if input is int and
if it is in range so row and column can be selected'''
def ask_int():
    while True:
        try:
            val = int(raw_input("Input: "))
            if(val < 0 or val >= len(grd)):
                print("Value out of range, please pick a valid number")
                continue
        except:
            print("No integer detected, please try again")
            continue
        else:
            return val
            break

#update_grid(a_grid)
'''
Ask current player to select a row and column.
Check if grid[row,col,playerID] != 'X' or 'O' (not set yet)
if not set yet, set it to X or O depending on player and return 0.
if set already, return 1
'''
def update_grid(a_grid):
    global turn_count
    print('Please pick a row: ')
    row = ask_int()
    print('Please pick a column: ')
    col = ask_int()
    if grd[row][col] != "[ ]":
        print("Position already taken, place pick another one.")
        return 1
    else:
        if turn_count%2 == 0:
            to_print = ["X"]
        else:
            to_print = ["O"]
    a_grid[row][col] = to_print
    print_grid(a_grid)
    return 0

'''Funtion that checks if winning pattern has occurred
returns True if so, returns False otherwise'''
def check_gameover(a_grid):

    #Check for 3 in a row horizontally
    for row in range(0, len(a_grid)):
        result = all(elem == a_grid[row][0] for elem in a_grid[row])
        if result:
            if(a_grid[row][0] == "[ ]"):
                return False
            else:
                print "We have a winner!"
                return True

    #Check for 3 in a row vertically
    zipped_grid = zip(a_grid[0], a_grid[1], a_grid[2])
    for zip_row in range(0, len(zipped_grid)):
        zip_result = all(elem == zipped_grid[zip_row][0] for elem in zipped_grid[zip_row])
        if zip_result:
            if (zipped_grid[zip_row][0] == "[ ]"):
                return False
            else:
                print "We have a winner!"
                return True

    #Check for 3 in a row diagonally
    #Option 1
    diag_values1 = [a_grid[0][0], a_grid[1][1], a_grid[2][2]]
    diag_result1 = all(elem == diag_values1[0] for elem in diag_values1)
    if diag_result1:
        if diag_values1[0] == "[ ]":
            return False
        else:
            print "We have a winner!"
            return True
    #Option 2
    diag_values2 = [a_grid[0][2], a_grid[1][1], a_grid[2][0]]
    diag_result2 = all(elem == diag_values2[0] for elem in diag_values2)
    if diag_result2:
        if diag_values2[0] == "[ ]":
            return False
        else:
            print "We have a winner!"
            return True

    #No winning pattern, keep playing
    else:
        return False

# turn_handler
'''print grid and update it each turn'''
def turn_handler(player1_name, player2_name):

    print_grid(grd)
    while   update_grid(grd) == True:
        pass

    return 0

# game_handler
'''
Calls turn handler, checks if gameover
'''
def game_handler():
    global turn_count
    global gameover
    global draw

    while turn_handler(player1_name, player2_name) == True:
        pass
    gameover = check_gameover(grd)
    turn_count+=1
    if turn_count == 9 and gameover == False:
        gameover = True
        print("It's a draw!")
        draw = True
    return gameover

#Main
print("Welcome to Tic Tac Toe!")
init_grid(grd)
player1_name = raw_input("Player 1, what is your name?")
player2_name = raw_input("Player 2, what is your name?")
players = [player1_name, player2_name]
print(random.choice(players) + ' may start!')
while  gameover == False:
    game_handler()


