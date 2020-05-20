###############################################################################################################
###############################################################################################################
##########################__FUNCTION TO_DETERMINE TURN ORDER__#################################################
###############################################################################################################
###############################################################################################################

# import random library to enable dice roll function.
from random import randint


# Use player "turn" boolean to manage while loop for determining turn order.
# These booleans will be useful later, during main game play.


def determine_turn_order():
    global red_player_turn
    global black_player_turn
    red_player_turn = False
    black_player_turn = False
    while red_player_turn == False and black_player_turn == False:
        # Die roll values are defined as a random integer between 1 and 6.
        input("Red player, press enter to roll die. ")
        die1 = randint(1, 6)
        print("Red player rolled a " + str(die1))
        input("Black player, press enter to roll die. ")
        die2 = randint(1, 6)
        print("Black player rolled a " + str(die2))
        # The player who rolls the higher number goes first. If roll values are equal, then prompt players to try again.
        # You can only exit this sequence if one player rolls higher than the other.
        if die1 > die2:
            print("Red player rolled a higher number. Red player goes first!")
            red_player_turn = True
            return red_player_turn
        elif die2 > die1:
            print("Black player rolled a higher number. Black player goes first!")
            black_player_turn = True
            return black_player_turn
        else:
            print("Both players rolled the same value. Try again!")


###############################################################################################################
###############################################################################################################
##############################__FUNCTION TO DEFINE ROLLING__###################################################
###############################################################################################################
###############################################################################################################

die1 = 0
die2 = 0
num_moves = 0
move_options = []
x = 0

def player_rolls():
    global num_moves
    global move_options
    global die1
    global die2
    if red_player_turn:
        player = "Red"
    else:
        player = "Black"
    # Prompt active player to roll the dice.
    input(player + " player, press enter to roll dice. ")
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    if die1 == die2:
        num_moves = 4
        move_options.append(die1)
        move_options.append(die1)
        move_options.append(die1)
        move_options.append(die1)
    else:
        num_moves = 2
        move_options.append(die1)
        move_options.append(die2)
    return move_options, die1, die2, num_moves


###############################################################################################################
###############################################################################################################
#########################################__FUNCTION_TO_ DRAW BOARD__###########################################
###############################################################################################################
###############################################################################################################

# Initialize number of tokens in play, and their locations, for both players.
# Note that I've effectively "unwrapped" a traditional backgammon board into one long line.
# The convention for spaces on the board is consistent between players/numbering of position is not directional.


# For each position on the board, look to see if there are any red or black tokens in play, and print their locations.
def board_update(board_array, player1_array, player2_array):
    for i in range(len(board_array)):
        if player1_array[i] > 0:
            board_array[i] = "R:0" + str(player1_array[i])
        elif player2_array[i] > 0:
            board_array[i] = "B:0" + str(player2_array[i])
        else:
            if i < 12:
                board_array[i] = "    "
            else:
                board_array[i] = "____"
    return board_array


# Define backgammon board graphics.
# There are 3 lines of the graphic that require input for red and black tokens in play/on the bar.
# The other lines are simply printed characters.
# I'll define the board graphic in terms of zones, so that I don't have to include all these characters in my script
# every time I print the graphic (which will be often).


def print_board(zone1, zone2, zone3, zone4, zone5, zone6, zone7):
    print(zone1)
    print(zone2)
    print(zone3)
    print(zone4)
    print(zone5)
    print(zone6)
    print(zone7)


###############################################################################################################
###############################################################################################################
############################################__MOVING TOKENS__##################################################
###############################################################################################################
###############################################################################################################
def determine_if_final(player_board):
    global is_final
    global red_player_turn
    if red_player_turn:
        is_final_array = [player_board[i] for i in range(6, 24)]
    else:
        is_final_array = [player_board[i] for i in range(0, 18)]
    if sum(is_final_array) == 0:
        is_final = True
    else:
        is_final = False
    return is_final

def token_move_final(player1_turn, player1_board, player2_board):
    global move_options
    global red_score
    global black_score
    token_pos = int(input("Select token to move/remove from board: "))
    if player1_turn:
        if player1_board[token_pos-1] > 0:
            if token_pos in move_options:
                red_score += 1
                player1_board[token_pos - 1] -= 1
                move_options.remove(token_pos)
                print("Red user score is now: " + str(red_score))
            else:
                user_selec_is_higher = [1 for i in range(0, len(move_options)) if token_pos > move_options[i]]
                if len(user_selec_is_higher) == len(move_options):
                    token_new_pos = int(input("Select new position for this token: "))
                    if token_new_pos > token_pos:
                        print("You can't move your token in that direction! Try again!")
                    elif token_new_pos < 1:
                        print("You can't move your token off the board like that! Try again!")
                    elif (token_pos - token_new_pos) in move_options:
                        player1_board[token_pos - 1] -= 1
                        player1_board[token_new_pos - 1] += 1
                        move_options.remove(token_pos - token_new_pos)
                        return move_options
                    else:
                        print("You have to move a token based on the dice roll values! Try again!")
                elif len(user_selec_is_higher) == 0:
                    tokens_in_higher_pos = [1 for i in range(token_pos, 6) if player1_board[i] > 1]
                    if len(tokens_in_higher_pos) > 0:
                        print("You cannot remove that token! You must move a token from a higher position on the board.")
                    else:
                        red_score += 1
                        player1_board[token_pos - 1] -= 1
                        move_options.remove(max(move_options))
                        print("Red user score is now: " + str(red_score))
                        return move_options, red_score
                else:
                    tokens_in_higher_pos = [1 for i in range(token_pos, 6) if player1_board[i] > 1]
                    if len(tokens_in_higher_pos) == 0:
                        red_score += 1
                        player1_board[token_pos - 1] -= 1
                        move_options.remove(max(move_options))
                        print("Red user score is now: " + str(red_score))
                    else:
                        token_new_pos = int(input("Select new position for this token: "))
                        if token_new_pos > token_pos:
                            print("You can't move your token in that direction! Try again!")
                        elif token_new_pos < 1:
                            print("You can't move your token off the board like that! Try again!")
                        elif (token_pos-token_new_pos) in move_options:
                            player1_board[token_pos - 1] -= 1
                            player1_board[token_new_pos - 1] += 1
                            move_options.remove(token_pos - token_new_pos)
                            return move_options
                        else:
                            print("You have to move a token based on the dice roll values! Try again!")
        else:
            print("You don't have a token there! Try again!")
    else:
        if player2_board[token_pos-1] > 0:
            if (25 - token_pos) in move_options:
                black_score += 1
                player2_board[token_pos - 1] -= 1
                move_options.remove(25 - token_pos)
                print("Black user score is now: " + str(black_score))
                return move_options, black_score
            else:
                user_selec_is_higher = [1 for i in range(0, len(move_options)) if (25 - token_pos) > move_options[i]]
                if len(user_selec_is_higher) == len(move_options):
                    token_new_pos = int(input("Select new position for this token: "))
                    if token_new_pos < token_pos:
                        print("You can't move your token in that direction! Try again!")
                    elif token_new_pos > 24:
                        print("You can't move your token off the board like that! Try again!")
                    elif (token_new_pos-token_pos) in move_options:
                        player2_board[token_pos - 1] -= 1
                        player2_board[token_new_pos-1] += 1
                        move_options.remove(token_new_pos - token_pos)
                        return move_options
                    else:
                        print("You have to move a token based on the dice roll values! Try again!")
                elif len(user_selec_is_higher) == 0:
                    tokens_in_higher_pos = [1 for i in range(19, token_pos) if player2_board[i - 1] > 1]
                    if sum(tokens_in_higher_pos) > 0:
                        print("You cannot remove that token! You must move a token from a lower position on the board.")
                    else:
                        black_score += 1
                        player2_board[token_pos - 1] -= 1
                        move_options.remove(max(move_options))
                        print("Black user score is now: " + str(black_score))
                        return move_options, black_score
                else:
                    tokens_in_higher_pos = [1 for i in range(19, token_pos) if player2_board[i - 1] > 1]
                    if len(tokens_in_higher_pos) == 0:
                        black_score += 1
                        player2_board[token_pos - 1] -= 1
                        move_options.remove(max(move_options))
                        print("Black user score is now: " + str(black_score))
                    else:
                        token_new_pos = int(input("Select new position for this token: "))
                        if token_new_pos < token_pos:
                            print("You can't move your token in that direction! Try again!")
                        elif token_new_pos > 24:
                            print("You can't move your token off the board like that! Try again!")
                        elif (token_new_pos-token_pos) in move_options:
                            player2_board[token_pos - 1] -= 1
                            player2_board[token_new_pos - 1] += 1
                            move_options.remove(token_new_pos - token_pos)
                            return move_options
                        else:
                            print("You have to move a token based on the dice roll values! Try again!")
        else:
            print("You don't have a token there! Try again!")

def token_move_bar(player1_turn, player1_board, player2_board):
    global move_options
    global red_bar
    global black_bar
    open_positions_return_from_bar = []
    available_bar_moves = []
    if player1_turn:
        positions_we_care_about = [19, 20, 21, 22, 23, 24]
        for i in positions_we_care_about:
            if player2_board[i-1] <= 1 and (25 - i) in move_options:
                available_bar_moves.append(i)
                print(available_bar_moves)
        if len(available_bar_moves) == 0:
            while len(move_options) > 0:
                move_options.pop()
            print("No valid moves! Sorry, your turn is over!")
        else:
            token_new_pos = int(input("Select a position to move the BAR token to: "))
            if token_new_pos in available_bar_moves:
                if player2_board[token_new_pos-1] == 1:
                    player2_board[token_new_pos-1] -= 1
                    black_bar += 1
                    print("Black player token goes to BAR!")
                player1_board[token_new_pos-1] += 1
                red_bar -= 1
                move_options.remove(25 - token_new_pos)
            else:
                print("You can't move a token there from BAR! Try again!")
    else:
        positions_we_care_about = [1, 2, 3, 4, 5, 6]
        for i in positions_we_care_about:
            if player1_board[i-1] <= 1 and i in move_options:
                open_positions_return_from_bar.append(i)
                available_bar_moves.append(i)
                print(available_bar_moves)
        if len(available_bar_moves) == 0:
            while len(move_options) > 0:
                move_options.pop()
            print("No valid moves! Sorry, your turn is over!")
        else:
            token_new_pos = int(input("Select a position to move the BAR token to: "))
            if token_new_pos in available_bar_moves:
                if player1_board[token_new_pos-1] == 1:
                    player1_board[token_new_pos-1] -= 1
                    red_bar += 1
                    print("Red player token goes to BAR!")
                player2_board[token_new_pos - 1] += 1
                black_bar -= 1
                move_options.remove(token_new_pos)
            else:
                print("You can't move a token there from BAR! Try again!")


def determine_game_state(player1_turn):
    global game_state
    global red_bar
    global black_bar
    global red_board
    global black_board
    if player1_turn:
        if red_bar > 0:
            game_state = "bar"
        else:
            determine_if_final(red_board)
            if is_final:
                game_state = "final"
            else:
                game_state = "normal"
    else:
        if black_bar > 0:
            game_state = "bar"
        else:
            determine_if_final(black_board)
            if is_final:
                game_state = "final"
            else:
                game_state = "normal"
    return game_state


def token_move_redux():
    global game_state
    global red_player_turn
    global red_board
    global red_score
    global black_board
    global black_score
    while len(move_options) > 0:
        if red_score < 15 and black_score < 15:
            print("Moves Available: " + str(move_options))
            determine_game_state(red_player_turn)
            if game_state == "bar":
                token_move_bar(red_player_turn, red_board, black_board)
            elif game_state == "final":
                token_move_final(red_player_turn, red_board, black_board)
            else:
                token_move_main(red_board, black_board)
        else:
            while len(move_options) > 0:
                move_options.pop()


def token_move_main(player1_board, player2_board):
    global x
    global move_options
    global red_bar
    global black_bar
    token_pos = int(input("Select a position from which to move a token: "))
    if red_player_turn:
        if player1_board[token_pos - 1] > 0:
            token_new_pos = int(input("Select a position to move the token to: "))
            x = abs(int(token_new_pos - token_pos))
            if x in move_options:
                if player2_board[token_new_pos - 1] > 1:
                    print("Your opponent has multiple tokens in that location! Try again!")
                elif token_new_pos > token_pos:
                    print("You can't move your token in that direction! Try again!")
                elif token_new_pos > 24 or token_new_pos < 1:
                    print("You can't move your token off the board! Try again!")
                elif player2_board[token_new_pos - 1] == 1:
                    black_bar += 1
                    player1_board[token_new_pos - 1] += 1
                    player1_board[token_pos - 1] -= 1
                    player2_board[token_new_pos - 1] -= 1
                    print("Black player token goes to BAR!")
                    move_options.remove(x)
                    return move_options
                else:
                    player1_board[token_new_pos - 1] += 1
                    player1_board[token_pos - 1] -= 1
                    move_options.remove(x)
                    return move_options
            else:
                print("You have to move a token based on the dice roll values! Try again!")
        else:
            print("Red player doesn't have a token there! Try again!")
    else:
        if player2_board[token_pos - 1] > 0:
            token_new_pos = int(input("Select a position to move the token to: "))
            x = abs(int(token_new_pos - token_pos))
            if x in move_options:
                if player1_board[token_new_pos - 1] > 1:
                    print("Your opponent has multiple tokens in that location! Try again!")
                elif token_new_pos < token_pos:
                    print("You can't move your token in that direction! Try again!")
                elif token_new_pos > 24 or token_new_pos < 1:
                    print("You can't move your token off the board! Try again!")
                elif player1_board[token_new_pos - 1] == 1:
                    red_bar += 1
                    player2_board[token_new_pos - 1] += 1
                    player2_board[token_pos - 1] -= 1
                    player1_board[token_new_pos - 1] -= 1
                    print("Red player token goes to BAR!")
                    x = abs(int(token_new_pos - token_pos))
                    move_options.remove(x)
                    return move_options
                else:
                    player2_board[token_new_pos - 1] += 1
                    player2_board[token_pos - 1] -= 1
                    x = abs(int(token_new_pos - token_pos))
                    move_options.remove(x)
                    return move_options
            else:
                print("You have to move a token based on the dice roll values! Try again!")
        else:
            print("Black player doesn't have a token there! Try again!")


###############################################################################################################
###############################################################################################################
#########################################__GENERAL_GAME_PLAY__#################################################
###############################################################################################################
###############################################################################################################

# Initialize slash instantiate all the things.

pos = ["    ", "    ", "    ", "    ", "    ", "    ", "    ", "    ", "    ", "    ", "    ", "    ",
       "____", "____", "____", "____", "____", "____", "____", "____", "____", "____", "____", "____"]
red_board = [0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
black_board = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0]
red_score = 0
black_score = 0
red_bar = 0
black_bar = 0
game_state = " "

# These are graphics for the board that will never change.
board_static_A = "          \n" \
                 "--->--->--->--->--->--->--->-BLACK PLAYER MOVES IN THIS DIRECTION-->--->--->--->--->--->--->--->--->--->--->--->-\n" \
                 "<---<---<---<---<---<---<---<-RED PLAYER MOVES IN THIS DIRECTION--<---<---<---<---<---<---<---<---<---<---<---<--\n" \
                 " _______________________________________________________________________________________________________________\n"\
                 "|                                                                                                               |\n"\
                 "|   [1]      [2]      [3]      [4]      [5]      [6]        [7]      [8]      [9]      [10]     [11]     [12]   |\n"\
                 "|_______________________________________________________________________________________________________________| \n"\
                 "| ________ ________ ________ ________ ________ ________ | ________ ________ ________ ________ ________ ________ |"

board_static_C = "|  \    /   \    /   \    /   \    /   \    /   \    /  |  \    /   \    /   \    /   \    /   \    /   \    /  |\n" \
                 "|   \  /     \  /     \  /     \  /     \  /     \  /   |   \  /     \  /     \  /     \  /     \  /     \  /   |\n" \
                 "|    \/       \/       \/       \/       \/       \/    |    \/       \/       \/       \/       \/       \/    |\n" \
                 "|_______________________________________________________________________________________________________________|\n" \
                 "|                                                                                                               |"

board_static_E = "|_______________________________________________________________________________________________________________|\n" \
                 "|                                                                                                               |\n" \
                 "|    /\       /\       /\       /\       /\       /\    |    /\       /\       /\       /\       /\       /\    |\n" \
                 "|   /  \     /  \     /  \     /  \     /  \     /  \   |   /  \     /  \     /  \     /  \     /  \     /  \   |\n" \
                 "|  /    \   /    \   /    \   /    \   /    \   /    \  |  /    \   /    \   /    \   /    \   /    \   /    \  |"

# This line will never change.
board_static_G = "|_______________________________________________________________________________________________________________|\n" \
                 "|                                                                                                               |\n" \
                 "|   [24]     [23]     [22]     [21]     [20]     [19]       [18]     [17]     [16]     [15]     [14]     [13]   |\n" \
                 "|_______________________________________________________________________________________________________________|\n" \
                 "--->--->--->--->--->--->--->-RED PLAYER MOVES IN THIS DIRECTION-->--->--->--->--->--->--->--->--->--->--->--->--->\n" \
                 "<---<---<---<---<---<---<---<-BLACK PLAYER MOVES IN THIS DIRECTION--<---<---<---<---<---<---<---<---<---<---<---<-\n" \
                 "             "

# Actual game play starts here.
determine_turn_order()

board_update(pos, red_board, black_board)

board_flex_B = "| \ " + pos[0] + " / \ " + pos[1] + " / \ " + pos[2] + " / \ " + pos[3] + " / \ " + pos[4] + " / \ " + \
               pos[5] + " / | \ " + pos[6] + " / \ " + pos[7] + " / \ " + pos[8] + " / \ " + pos[9] + " / \ " + pos[
                   10] + \
               " / \ " + pos[11] + " / |"
board_flex_D = "|                                                BAR - R: " + str(red_bar) + "  B: " + str(black_bar) + \
               "                                               |"
board_flex_F = "| /_" + pos[23] + "_\ /_" + pos[22] + "_\ /_" + pos[21] + "_\ /_" + pos[20] + "_\ /_" + pos[19] + \
               "_\ /_" + pos[18] + "_\ | /_" + pos[17] + "_\ /_" + pos[16] + "_\ /_" + pos[15] + "_\ /_" + pos[14] + \
               "_\ /_" + pos[13] + "_\ /_" + pos[12] + "_\ |"

is_final = False

while red_score < 15 and black_score < 15:
    player_rolls()
    print_board(board_static_A, board_flex_B, board_static_C, board_flex_D,
                board_static_E, board_flex_F, board_static_G)
    if red_player_turn:
        print("Red player rolled a " + str(die1) + " and a " + str(die2) + ".")
        print("Red player, you have " + str(num_moves) + " moves this turn.")
    else:
        print("Black player rolled a " + str(die1) + " and a " + str(die2) + ".")
        print("Black player, you have " + str(num_moves) + " moves this turn.")

    token_move_redux()

    if red_player_turn:
        red_player_turn = False
        black_player_turn = True
    else:
        red_player_turn = True
        black_player_turn = False

    board_update(pos, red_board, black_board)

    board_flex_B = "| \ " + pos[0] + " / \ " + pos[1] + " / \ " + pos[2] + " / \ " + pos[3] + " / \ " + pos[4] + \
                   " / \ " + pos[5] + " / | \ " + pos[6] + " / \ " + pos[7] + " / \ " + pos[8] + " / \ " + pos[9] + \
                   " / \ " + pos[10] + " / \ " + pos[11] + " / |"
    board_flex_D = "|                                                BAR - R: " + str(red_bar) + "  B: " + str(
        black_bar) + "                                               |"
    board_flex_F = "| /_" + pos[23] + "_\ /_" + pos[22] + "_\ /_" + pos[21] + "_\ /_" + pos[20] + "_\ /_" + pos[19] + \
                   "_\ /_" + pos[18] + "_\ | /_" + pos[17] + "_\ /_" + pos[16] + "_\ /_" + pos[15] + "_\ /_" + pos[14] + \
                   "_\ /_" + pos[13] + "_\ /_" + pos[12] + "_\ |"

    print_board(board_static_A, board_flex_B, board_static_C, board_flex_D,
                board_static_E, board_flex_F, board_static_G)

if red_score > black_score:
    print("\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print("~*~*~*~*~*~*~*~*~ Red player wins!!! *~*~*~*~*~*~*~*~")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
else:
    print("\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print("~*~*~*~*~*~*~*~ Black player wins!!! *~*~*~*~*~*~*~*~")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
