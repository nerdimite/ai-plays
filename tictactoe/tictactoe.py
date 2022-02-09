from time import sleep
import random
from gameplay import Gameplay
from terminal_utils import write, print_win, print_error, print_tie, print_info

game = Gameplay()

print("———————————————————————————————————————————")
print("\t\t\033[31mTIC \033[32mTAC\033[33m TOE\033[0m")
print("———————————————————————————————————————————\n")

# Show the instructions
game.print_help()

# Confirm to start the game
while(1):
    begin = input("\033[32mStart the Game? (y/n): \033[0m")
    if begin == 'y':
        break
    elif begin == 'n':
        print('Game Exited')
        exit()
    else:
        continue

# Coin toss of who goes first
players = ['X', 'O']
write('Tossing the Coin... ')
for _ in range(10):
    for p in players:
        write(f'{p}')
        sleep(0.1)
        write('\b')
write('\033[2K\r')
random.shuffle(players)
print(f"\nCoin Toss Resulted in \033[32m{players[0]}\033[0m going first!")


game.print_board()


while(1):

    for action in players:

        while(1):
            position = input(
                f'Player \033[32m{action}\033[0m Enter Board Position: ')
            position = position.upper().strip()

            # validate the inputs
            if position not in game.board.keys():
                write("\033[B\r")
                print_error(
                    f"{position} is invalid position")
                write("\033[A\033[2K\r")
                continue
            else:
                write("\033[A\033[2K\r")

            if game.board[position] is not None:
                print_error(f"{game.board[position]} is already at {position}")
                continue

            game.take_action(position, action)
            sleep(0.1)

            game.board[position] = action

            if game.check_win():
                print_win(game.winner)
                exit()

            break

        if all(game.board[pos] != None for pos in game.board.keys()):
            print_tie()
            exit()
