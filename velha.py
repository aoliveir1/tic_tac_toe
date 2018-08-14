# -*- coding: utf-8 -*-
import random
import time

def get_data():
    return 'Você é: {}\nO Pc é: {}'.format(sVC, sPC)

def print_matrix(matrix):
    # Create the board.
    print('\n')
    print('', matrix[0][0], matrix[0][1], matrix[0][2], '', sep="  ")
    print('', matrix[1][0], matrix[1][1], matrix[1][2], '', sep="  ")
    print('', matrix[2][0], matrix[2][1], matrix[2][2], '', sep="  ")
    print('\n')

def get_position(pos):
    # Call this when the user input the board position to get the coords.
    if pos == 1: return [0, 0]
    elif pos == 2: return [0, 1]
    elif pos == 3: return [0, 2]
    elif pos == 4: return [1, 0]
    elif pos == 5: return [1, 1]
    elif pos == 6: return [1, 2]
    elif pos == 7: return [2, 0]
    elif pos == 8: return [2, 1]
    elif pos == 9: return [2, 2]
    else:
        return False

def draw(matrix):
    # Return when the board is full and nobody wins.
    if '_' not in matrix[0] and '_' not in matrix[1] and '_' not in matrix[2]: return True

def is_winner(simbol, matrix):
    # Check if a row, column or diagonal is complete
    if matrix[0][0] == simbol and matrix[0][1] == simbol and matrix[0][2] == simbol: return True
    if matrix[1][0] == simbol and matrix[1][1] == simbol and matrix[1][2] == simbol: return True
    if matrix[2][0] == simbol and matrix[2][1] == simbol and matrix[2][2] == simbol: return True
    if matrix[0][0] == simbol and matrix[1][0] == simbol and matrix[2][0] == simbol: return True
    if matrix[0][1] == simbol and matrix[1][1] == simbol and matrix[2][1] == simbol: return True
    if matrix[0][2] == simbol and matrix[1][2] == simbol and matrix[2][2] == simbol: return True
    if matrix[0][0] == simbol and matrix[1][1] == simbol and matrix[2][2] == simbol: return True
    if matrix[0][2] == simbol and matrix[1][1] == simbol and matrix[2][0] == simbol: return True

def one_left(simbol, matrix):
    # Check if there is only one left to complete, for two things:
    # If the bot is about to win the game: suggest playing in the right field to win.
    # If the human player is about to win the game: suggest the bot to play in the right field to not lose.
    if matrix[0][0] == simbol and matrix[0][1] == simbol:
        if matrix[0][2] == '_': return 3
    if matrix[0][0] == simbol and matrix[0][2] == simbol:
        if matrix[0][1] == '_': return 2
    if matrix[0][1] == simbol and matrix[0][2] == simbol:
        if matrix[0][0] == '_': return 1

    if matrix[1][0] == simbol and matrix[1][1] == simbol:
        if matrix[1][2] == '_': return 6
    if matrix[1][0] == simbol and matrix[1][2] == simbol:
        if matrix[1][1] == '_': return 5
    if matrix[1][1] == simbol and matrix[1][2] == simbol:
        if matrix[1][0] == '_': return 4

    if matrix[2][0] == simbol and matrix[2][1] == simbol:
        if matrix[2][2] == '_': return 9
    if matrix[2][0] == simbol and matrix[2][2] == simbol:
        if matrix[2][1] == '_': return 8
    if matrix[2][1] == simbol and matrix[2][2] == simbol:
        if matrix[2][0] == '_': return 7

    if matrix[0][0] == simbol and matrix[1][0] == simbol:
        if matrix[2][0] == '_': return 7
    if matrix[0][0] == simbol and matrix[2][0] == simbol:
        if matrix[1][0] == '_': return 4
    if matrix[1][0] == simbol and matrix[2][0] == simbol:
        if matrix[0][0] == '_': return 1

    if matrix[1][0] == simbol and matrix[1][1] == simbol:
        if matrix[2][1] == '_': return 8
    if matrix[1][0] == simbol and matrix[2][1] == simbol:
        if matrix[1][1] == '_': return 5
    if matrix[1][1] == simbol and matrix[2][1] == simbol:
        if matrix[0][1] == '_': return 2

    if matrix[0][1] == simbol and matrix[1][1] == simbol:
        if matrix[2][1] == '_': return 8
    if matrix[0][1] == simbol and matrix[2][1] == simbol:
        if matrix[1][1] == '_': return 5
    if matrix[1][1] == simbol and matrix[2][1] == simbol:
        if matrix[0][1] == '_': return 2

    if matrix[0][2] == simbol and matrix[1][2] == simbol:
        if matrix[2][2] == '_': return 9
    if matrix[0][2] == simbol and matrix[2][2] == simbol:
        if matrix[1][2] == '_': return 6
    if matrix[1][2] == simbol and matrix[2][2] == simbol:
        if matrix[0][2] == '_': return 3

    if matrix[0][0] == simbol and matrix[1][1] == simbol:
        if matrix[2][2] == '_': return 9
    if matrix[0][0] == simbol and matrix[2][2] == simbol:
        if matrix[1][1] == '_': return 5
    if matrix[1][1] == simbol and matrix[2][2] == simbol:
        if matrix[0][0] == '_': return 1

    if matrix[0][2] == simbol and matrix[1][1] == simbol:
        if matrix[2][0] == '_': return 7
    if matrix[0][2] == simbol and matrix[2][0] == simbol:
        if matrix[1][1] == '_': return 5
    if matrix[1][1] == simbol and matrix[2][0] == simbol:
        if matrix[0][2] == '_': return 3

def prevent(simbol, matrix):
    # Sugest to the bot to play in a field of a free row/column/diagonal
    if matrix[0][0] == simbol: return [6, 8]
    if matrix[0][1] == simbol: return [4, 6, 9]
    if matrix[0][2] == simbol: return [4, 8]
    if matrix[1][0] == simbol: return [2, 3, 8, 9]
    if matrix[1][2] == simbol: return [2, 3, 7, 8]
    if matrix[2][0] == simbol: return [3, 6, 8, 9]
    if matrix[2][1] == simbol: return [2, 3, 4, 6]
    if matrix[2][2] == simbol: return [2, 4]
    #if matrix[1][1] == simbol: pass

tie = 0
you_win = 0
you_lose = 0
op = True

while op:
    vec1 = ['_', '_', '_']
    vec2 = ['_', '_', '_']
    vec3 = ['_', '_', '_']
    matrix = [vec1, vec2, vec3]

    player = random.choice((0, 1))

    if player == 1:
        sVC = 'X'
        sPC = 'O'
    else:
        sPC = 'X'
        sVC = 'O'
    turn = 0
    game = True
    while game:
        turn += 1
        if draw(matrix):
            print_matrix(matrix)
            tie+=1
            game = False
            print("VELHA")
            break
        if player:
            while 1:
                pc = None
                while pc is None:
                    try:
                        print_matrix(matrix)
                        print(get_data())
                        pc = int(input('Você que joga: '))
                        if (pc > 0 and pc < 10):
                            pos = get_position(pc)
                        else:
                            print('Posição inválida!')
                    except ValueError:
                        print('Entrada inválida!')

                if matrix[pos[0]][pos[1]] == '_':
                    break
                else:
                    print('Espaço já ocupado!')

            matrix[pos[0]][pos[1]] = sVC
            player = 0

            if is_winner(sVC,matrix):
                print_matrix(matrix)
                print('VC GANHOU! TECLE ENTER PARA CONTINUAR!')
                you_win+=1
                game = False
                break

        else:
            print_matrix(matrix)
            print(get_data())
            print('Pc que joga:')
            time.sleep(1)
            pc = 0
            while 1:
                if one_left(sPC,matrix):
                    pc = one_left(sPC, matrix)
                elif one_left(sVC, matrix):
                    pc = one_left(sVC, matrix)
                elif turn < 5 and prevent(sVC, matrix):
                    pc = random.choice(prevent(sVC, matrix))
                else:
                    pc = random.randint(1, 9)

                pos = get_position(pc)
                if matrix[pos[0]][pos[1]] == '_':
                    break

            matrix[pos[0]][pos[1]] = sPC

            player = 1

            if is_winner(sPC,matrix):
                print_matrix(matrix)
                you_lose+=1
                game = False
                input('VC PERDEU! TECLE ENTER PARA CONTINUAR!')
                break

    print(('\nPlacar:\n\tVelha = {}\n\tVocê = {}\n\tPc = {}').format(tie,you_win,you_lose))
    op = input('Tecle \'s\' e \'enter\' para jogar mais uma.')
    if op != 's':
        op = False
