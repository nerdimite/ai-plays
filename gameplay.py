from terminal_utils import write, print_info

# Mapping of board position to cursor action
CURSOR_ACTIONS = {
    'T1': {
        'up': 6,
    },
    'T2': {
        'right': 4,
        'up': 6
    },
    'T3': {
        'right': 8,
        'up': 6
    },
    'M1': {
        'up': 4,
    },
    'M2': {
        'right': 4,
        'up': 4,
    },
    'M3': {
        'right': 8,
        'up': 4,
    },
    'B1': {
        'up': 2,
    },
    'B2': {
        'right': 4,
        'up': 2,
    },
    'B3': {
        'right': 8,
        'up': 2,
    },
}


class Gameplay():
    '''TicTacToe Gameplay Utilities'''

    def __init__(self):
        self.board = {
            'T1': None, 'T2': None, 'T3': None,
            'M1': None, 'M2': None, 'M3': None,
            'B1': None, 'B2': None, 'B3': None
        }
        self.winner = None

    def print_board(self):
        print()
        print("   |   |   ")
        print("———————————")
        print("   |   |   ")
        print("———————————")
        print("   |   |   ")
        print()

    def print_help(self):
        print("\033[36m————————————————Instructions————————————————\033[0m\n")
        print("\033[33mBoard Position Reference\033[0m\n")
        print(" T1 | T2 | T3 ")
        print("——————————————")
        print(" M1 | M2 | M3 ")
        print("——————————————")
        print(" B1 | B2 | B3 ")
        print("\nPlayers need to choose the respective position, as shown above, when its their turn.")
        print("\n\033[36m————————————————————————————————————————————\033[0m\n")

    def move(self, n, direction):
        '''Move to a particular position in the terminal
        Args:
            n (int): Number of positions to move
            direction (str): Direction to move in the terminal
        '''
        if direction == 'up':
            write(f"\033[{n}A")
        elif direction == 'down':
            write(f"\033[{n}B")
        elif direction == 'right':
            write(f"\033[{n}C")
        elif direction == 'left':
            write(f"\033[{n}D")

    def take_action(self, position, action):
        '''
        Takes a X or O action on a particular position on the board
        Args:
            position (str): Choose from [T1, T2, T3, M1, M2, M3, B1, B2, B3]
            action (str): Choose between [X | O]
        '''
        moves = CURSOR_ACTIONS[position]
        for d, n in moves.items():
            self.move(n, d)
        write(f" {action} ")
        write("\n" * moves['up'])

    def check_win(self):
        '''Returns True if any player has won in the current board state'''

        rows = ['T', 'M', 'B']
        cols = ['1', '2', '3']

        # check horizontal
        for r in rows:
            for player in ['X', 'O']:
                if all([self.board[r+c] == player for c in cols]):
                    for c in cols:
                        self.take_action(r+c, f'\033[32m{player}\033[0m')
                    self.winner = player
                    return True

        # check vertical
        for c in cols:
            for player in ['X', 'O']:
                if all([self.board[r+c] == player for r in rows]):
                    for r in rows:
                        self.take_action(r+c, f'\033[32m{player}\033[0m')
                    self.winner = player
                    return True

        # check left-right diagonal
        for player in ['X', 'O']:
            if all([self.board[r+c] == player for r, c in zip(rows, cols)]):
                for r, c in zip(rows, cols):
                    self.take_action(r+c, f'\033[32m{player}\033[0m')
                self.winner = player
                return True

        # check right-left diagonal
        for player in ['X', 'O']:
            if all([self.board[r+c] == player for r, c in zip(rows, cols[::-1])]):
                for r, c in zip(rows, cols[::-1]):
                    self.take_action(r+c, f'\033[32m{player}\033[0m')
                self.winner = player
                return True

        return False
