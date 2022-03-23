# command version of simple tictactoe using python

# game board
board = [ '-' for _ in range(9)]


# some initialization
game_still_on = True      # keep track if game is over or not
winner = None             # contain winner
current_player = 'X'      # either 'X' or 'O'


# function to print a board
def print_board():
  j = 1       # counter for number to show in board
  num_board = [board[i*3:(i+1)*3] for i in range(3)] # num board contains three list within a list i.e [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
  for i in num_board:
    print("| " + " | ".join(i) + " |" + f'      | {j} | {j+1} | {j+2} |')
    j += 3


# main function for game
def tictactoe():
  print_board()
  while(game_still_on):
    turn_handler(current_player)
    
    game_over()
    
    flip_player()
  
  if winner == None:
    print("Tie.")
  else:
    print(f"{winner} won.")
  

# this function does same thing for each player every time
# this mainly handles the turn
def turn_handler(current_player):
  print(f'{current_player}\'s turn')
  valid = True  # keep track if position is valid or not
  while valid:
    position = input("Choose a number from 0 to 9 : ")
    while position not in [str(i) for i in range(9)]:   #check if input is between 1 - 9
      position = input("Choose a number from 0 to 9 : ")
    position = int(position) - 1
    if board[position] == '-':
      board[position] = current_player
      valid = False
    else:
      print("You have already used that position")
    print_board()


# check if game is over or not
# and if there is winner assign a winner and if not tie
def game_over():
  check_for_win()
  check_for_tie()
  

def check_for_win():
  global winner
  row_winner = check_row_winner()
  col_winner = check_col_winner()
  dig_winner = check_dig_winner()
  if row_winner:
    winner = row_winner
  elif col_winner:
    winner = col_winner
  elif dig_winner:
    winner = dig_winner
  else:
    winner = None
  
  
def check_row_winner():
  global game_still_on
  j = 0
  for i in range(3):
    # checking if row have same value or not
    if board[j] == board[j+1] == board[j+2] != '-': 
      game_still_on = False
      return board[j]
    j += 3


def check_col_winner():
  global game_still_on
  j = 0
  for i in range(3):
    # checking if column have same value or not
    if board[j] == board[j+3] == board[j+6] != '-': 
      game_still_on = False
      return board[j]
    j += 1
  return None


def check_dig_winner():
  global game_still_on
  # checking if diagonal have same value or not
  dig1 = board[0] == board[4] == board[8] != '-'
  dig2 = board[2] == board[4] == board[6] != '-'
  if dig1 or dig2:
    game_still_on = False
  if dig1:
    return board[0]
  elif dig2:
    return board[2]
  else:
    return None

  
def check_for_tie():
  global game_still_on
  if winner == None and '-' not in board:
    game_still_on = False
  

# Toggle between players
def flip_player():
  global current_player
  # toggling between players.
  current_player = 'X' if current_player == 'O' else 'O'
  

tictactoe()