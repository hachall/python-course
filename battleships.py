# from IPython.display import clear_output
import random
from time import sleep
import os

def clear_output():
  os.system('clear')

class Ship():
    lengths = {'Aircraft Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Destroyer': 2, 'Submarine': 1}

    def __init__(self, ship_type):
        self.type = ship_type
        self.length = Ship.lengths[ship_type]
        self.lives = Ship.lengths[ship_type]
        self.coords = []

    def __str__(self):
        return self.type

class Grid():

    lengths = {'Aircraft Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Destroyer': 2, 'Submarine': 1}

    def __init__(self, size, override_fleet=False):
        self.grid_w_ships = [[]] + [['#'] + ['O' for x in range(1,size+1)] for x in range(1,size+1)]
        self.grid_wo_ships = [[]] + [['#'] + ['O' for x in range(1,size+1)] for x in range(1,size+1)]
        self.size = size
        self.fleet = []
        ship_list = ['Aircraft Carrier', 'Battleship', 'Cruiser', 'Destroyer', 'Destroyer', 'Submarine', 'Submarine']

        if override_fleet:
            ship_list = override_fleet

        for ship in ship_list:
            self.fleet.append(Ship(ship))
        life_sum = 0
        for ship in self.fleet:
            life_sum += ship.length
        self.lives = life_sum

    def display_board(self, board):
        for line in board:
            print(' '.join(line[1:]))

    def invalid_coord(self, coord):
        if coord.isdigit():
            if int(coord) > self.size:
                print("Value out of range! Please pick co-ordinates again")
                return True
            else:
                return False
        else:
            print(f"Invalid input! Enter a number 1-{self.size}")
            return True

    def invalid_range(self, placement_info):
        x, y, direction, ship = placement_info
        if direction == 'h':
            return x + ship.length > self.size+1
        else:
            return y + ship.length > self.size+1

    def invalid_availability(self, placement_info):
        x, y, direction, ship = placement_info
        if direction == 'h':
            counter = 0
            for _ in range(ship.length):
                if self.grid_w_ships[y][x + counter] == '-' or self.grid_w_ships[y][x + counter] == '|':
                    return True
                counter += 1
            else:
                return False
        else:
            counter = 0
            for _ in range(ship.length):
                if self.grid_w_ships[y + counter][x] == '-' or self.grid_w_ships[y + counter][x] == '|':
                    return True
                counter += 1
            else:
                return False

    def place_ship(self, placement_info):
        x, y, direction, ship = placement_info
        if direction == 'h':
            counter = 0
            for _ in range(ship.length):
                self.grid_w_ships[y][x + counter] = '-'
                ship.coords.append((x+counter, y))
                counter += 1
        else:
            counter = 0
            for _ in range(ship.length):
                self.grid_w_ships[y + counter][x] = '|'
                ship.coords.append((x, y+counter))
                counter += 1

    def initialize_ships(self):
        print("For each ship you will pick a starting co-ordinate (x,y) and a direction (h/v)")
        counter = 0
        for ship in self.fleet:

            while True:

                if counter == 0:
                    self.display_board(self.grid_w_ships)

                print(f"where would you like to place your {ship}. It has a length of {ship.length}")

                x = input(f"What x co-ordinate do you choose (1-{self.size})")
                while self.invalid_coord(x):
                    x = input(f"What x co-ordinate do you choose (1-{self.size})")

                y = input(f"What y co-ordinate do you choose (1-{self.size})")
                while self.invalid_coord(y):
                    y = input(f"What y co-ordinate do you choose (1-{self.size})")

                x = int(x)
                y = int(y)

                direction = input("Would you like to place the ship horizontally (h) or vertically (v)")

                while not(direction[0].lower() == 'h') and not(direction[0].lower() == 'v'):
                    print("incorrect input - type 'h' or 'v'")
                    direction = input("Would you like to place the ship horizontally (h) or vertically (v)")

                placement_tuple = (x, y, direction, ship)

                if self.invalid_range(placement_tuple):
                    print("This ship goes out of bounds. Try place it again:")
                    continue

                if self.invalid_availability(placement_tuple):
                    print("This is an invalid placement! It overlaps one of your other ships. Try place it again:")
                    continue

                self.place_ship(placement_tuple)
                print("Your ship has been placed:")
                self.display_board(self.grid_w_ships)
                counter += 1
                break

    def take_guess(self):
        print(f"Where would you like to bomb:")
        x = input(f"What x co-ordinate do you choose (1-{self.size})")
        while self.invalid_coord(x):
            x = input(f"What x co-ordinate do you choose (1-{self.size})")

        y = input(f"What y co-ordinate do you choose (1-{self.size})")
        while self.invalid_coord(y):
            y = input(f"What y co-ordinate do you choose (1-{self.size})")

        return (int(x), int(y))

    def bomb(self, coords):
        x, y = coords

        if self.grid_w_ships[y][x] == '-' or self.grid_w_ships[y][x] == '|':
            self.grid_w_ships[y][x] = 'X'
            self.grid_wo_ships[y][x] = 'X'
            self.lives -= 1
            for ship in self.fleet:
                if (x,y) in ship.coords:
                    ship.lives -= 1
            return True

        elif self.grid_w_ships[y][x] == 'X':
            return False

        else:
            self.grid_w_ships[y][x] = ' '
            self.grid_wo_ships[y][x] = ' '
            return False

def turn_logic(turn, attacking, passive):
    playing = ['', 'Player 1', 'Player 2'][turn]
    other_player = ['', 'Player 1', 'Player 2'][turn * -1]

    print(f"{playing}'s turn:")
    print("\n")
    print("Your grid:")
    attacking.display_board(attacking.grid_w_ships)
    print("\n")
    print(f"{other_player}'s grid:")
    passive.display_board(passive.grid_wo_ships)

    coords = passive.take_guess()
    success = passive.bomb(coords)

    clear_output()
    print(f"{playing}s turn:")
    print("\n")
    print("Your grid:")
    attacking.display_board(attacking.grid_w_ships)
    print("\n")
    print(f"{other_player}'s grid:")
    passive.display_board(passive.grid_wo_ships)

    if success:
        print("you hit!")
        for ship in passive.fleet:
            if ship.lives ==0:
                print(f"you destroyed their {ship.type}")
        if passive.lives == 0:
            print(f"you destroyed all of {other_player}'s fleet!")
            print(f"{playing} wins")
            return False
    else:
        print("unlucky you missed")

    input("when you're ready - press 'enter'")
    clear_output()
    sleep(3)
    return True

def game():
    print("Welcome to Battleships!")
    print("Take it in turns to try bomb each other's fleet")
    while True:
        try:
            grid_size = int(input("How large a grid would you like to play on:"))
            break
        except:
            print("invalid input - put a number (preferably 10 or under)")

    player1 = Grid(grid_size)
    player2 = Grid(grid_size)

    print("it's Player 1s turn to place their ships")
    player1.initialize_ships()
    print("ships placed")
    input("when you're happy, press 'enter' and pass the computer to Player 2")

    clear_output()
    sleep(2)

    print("it's Player 2s turn to place their ships")
    player2.initialize_ships()
    print("ships placed")
    input("when you're happy, press 'enter'")

    clear_output()

    print("time to take turns bombing co-ordinates (x,y)")
    print("win by wiping out your opponent's fleet before they get yours!")
    print("at the end of your go you will be prompted to press enter - make sure to pass over to the next player without looking at their ships! (there will be a 3s delay)")

    print("picking random player to start ...")
    sleep(4)
    turn = [1, -1][random.randint(0,1)]
    player = ['', 'Player 1', 'Player 2'][turn]

    print(f"{player} will go first!")

    input("when you're ready - press 'enter'")

    clear_output()

    game_on = True
    while game_on:

        if turn == 1:
            game_on = turn_logic(turn, player1, player2)
            turn *= -1
        else:
            game_on = turn_logic(turn, player2, player1)
            turn *= -1

    print("thank you for playing battleships")
    print("Final board's:")
    print("\n")
    print("Player 1 grid:")
    player1.display_board(player1.grid_w_ships)
    print("\n")
    print("Player 2's grid:")
    player2.display_board(player2.grid_w_ships)

while True:
    game()

    replay = input("would you like to play again?")
    if replay[0].lower() == 'y':
        continue
    break

clear_output()
print('thank you')


