def is_valid_move_red(token_pos, token_new_pos, move_options):
    """A function to determine if a token move is valid (red player only)."""

    if token_new_pos > token_pos:
        print("You can't move your token in that direction! Try again!")

    elif token_new_pos < 1:
        print("You can't move your token off the board like that! Try again!")

    elif (token_pos-token_new_pos) in move_options:
        return True

    else:
        print("You have to move a token based on the dice roll values! Try again!")

    return False


def token_move_final_red(move_options, red_score, player1_board):

    while move_options != []:
        
        token_pos = int(input("Select token to move/remove from board: "))

        if player1_board[token_pos-1] > 0:

            if token_pos in move_options:
                red_score += 1
                player1_board[token_pos - 1] -= 1
                move_options.remove(token_pos)
                print(f'Red user score is now: {red_score}')

            else:
                user_selec_is_higher = [1 for i in range(0, len(move_options)) if token_pos > move_options[i]]

                if len(user_selec_is_higher) == len(move_options):
                    
                    token_new_pos = int(input("Select new position for this token: "))

                    if is_valid_move_red(token_pos, token_new_pos, move_options):
                            player1_board[token_pos - 1] -= 1
                            player1_board[token_new_pos - 1] += 1
                            move_options.remove(token_pos - token_new_pos)

                elif len(user_selec_is_higher) == 0:
                    tokens_in_higher_pos = [1 for i in range(token_pos, 6) if player1_board[i] > 1]
                    if len(tokens_in_higher_pos) > 0:
                        print("You cannot remove that token! You must move a token from a higher position on the board.")
                    else:
                        red_score += 1
                        player1_board[token_pos - 1] -= 1
                        move_options.remove(max(move_options))
                        print(f'Red user score is now: {red_score}')
                else:
                    tokens_in_higher_pos = [1 for i in range(token_pos, 6) if player1_board[i] > 1]
                    if len(tokens_in_higher_pos) == 0:
                        red_score += 1
                        player1_board[token_pos - 1] -= 1
                        move_options.remove(max(move_options))
                        print(f'Red user score is now: {red_score}')
                    else:
                        token_new_pos = int(input("Select new position for this token: "))
                        
                        if is_valid_move_red(token_pos, token_new_pos, move_options):
                            player1_board[token_pos - 1] -= 1
                            player1_board[token_new_pos - 1] += 1
                            move_options.remove(token_pos - token_new_pos)
        else:
            print("You don't have a token there! Try again!")
    
    return red_score



def token_move_final_black(move_options, black_score, player2_board):

    token_pos = int(input("Select token to move/remove from board: "))
    if player2_board[token_pos-1] > 0:
        if (25 - token_pos) in move_options:
            black_score += 1
            player2_board[token_pos - 1] -= 1
            move_options.remove(25 - token_pos)
            print(f'Black user score is now: {black_score}')
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
                    print(f'Black user score is now: {black_score}')
                    return move_options, black_score
            else:
                tokens_in_higher_pos = [1 for i in range(19, token_pos) if player2_board[i - 1] > 1]
                if len(tokens_in_higher_pos) == 0:
                    black_score += 1
                    player2_board[token_pos - 1] -= 1
                    move_options.remove(max(move_options))
                    print(f'Black user score is now: {black_score}')
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