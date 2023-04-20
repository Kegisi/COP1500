"""
Integration Project
Professor Michael Osheroff
COP 1500
February 2023
"""
__author__ = "Dennis Kerry"

import msvcrt
import random
import constants
import os


class GameEntity:
    """
    Any character that is within the game
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        """
        Changes the coords of the object based on a directional value
        :param direction: A string in all lowercase
        """

        if direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1
        elif direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1

        # make sure the object does not move beyond the borders of the window
        if self.x <= 0:
            self.x = 1
        elif self.x > constants.WINDOW_WIDTH:
            self.x = constants.WINDOW_WIDTH
        elif self.y <= 0:
            self.y = 1
        elif self.y > constants.WINDOW_HEIGHT:
            self.y = constants.WINDOW_HEIGHT

    def check_adjacency(self, entity):
        """
        :param entity: The entity to check adjacency
        :return: The distance between the two objects
        """
        if abs(self.x - entity.x) == 1 and abs(self.y - entity.y) == 1:
            return True
        else:
            return False

    def check_collision(self, entity):
        """
        :param entity: The entity to check collision with
        :return: True if the objects are overlapping
        """
        if self.x == entity.x and self.y == entity.y:
            return True
        else:
            return False


class Player(GameEntity):
    """
    The player that will be defined by an @ sign
    """
    pass


class Orc(GameEntity):
    """
    Orcs will be the enemies and will be defined by an o sign
    """
    pass


class Game:
    def __init__(self):
        self.turn_counter = 0

    def update_screen(self):
        """
        Prints the grid and all the characters
        :return: none
        """
        os.system('cls')  # Clears the console of all previous frames
        # The play area is printed using periods for each space (temporary for
        # visualizing)
        orc_should_be_here = False
        for current_y_pos in range(constants.WINDOW_HEIGHT):
            for current_x_pos in range(constants.WINDOW_WIDTH):
                # For each orc, print o
                for current_orc in range(constants.AMOUNT_OF_ORCS):
                    if ((current_x_pos + 1) == self.orc[current_orc].x) \
                            and (
                            (current_y_pos + 1) == self.orc[current_orc].y):
                        orc_should_be_here = True

                # This line of code will print @ where the current player
                # coords are
                if ((current_x_pos + 1) == self.player.x) and (
                        (current_y_pos + 1) == self.player.y):
                    print('@', end=' ')
                    orc_should_be_here = False
                elif orc_should_be_here:
                    print('o', end=' ')
                    orc_should_be_here = False
                else:
                    print('.', end=' ')
            print()
        print("Turn:", format(self.turn_counter,
                              str(constants.WINDOW_WIDTH * 2 - 7) + '.0f'))
        self.turn_counter += 1

    # Create the player and divide the window dimensions by two to center it
    player = Player(constants.WINDOW_WIDTH // 2, constants.WINDOW_HEIGHT // 2)

    # Create the orcs
    orc = []
    for orc_number in range(constants.AMOUNT_OF_ORCS):
        orc_x = random.randint(1, constants.WINDOW_WIDTH)
        orc_y = random.randint(1, constants.WINDOW_HEIGHT)
        # Re-generate coords if they're the same as the player's
        while (orc_x == player.x) and (orc_y == player.y):
            orc_x = random.randint(1, constants.WINDOW_WIDTH)
            orc_y = random.randint(1, constants.WINDOW_HEIGHT)
        # Make sure the orc isn't being spawned in the same spot as another
        for orc_index in range(len(orc)):
            while (orc_x == orc[orc_index].x) and (orc_y == orc[orc_index].y):
                orc_x = random.randint(1, constants.WINDOW_WIDTH)
                orc_y = random.randint(1, constants.WINDOW_HEIGHT)
                orc_index = -1  # next iteration of the loop will start at 0
        orc.append(Orc(orc_x, orc_y))


def execute_code_from_sprint1():
    """
    this is just a function that contains all the requirements from Sprint 1
    :return: nothing
    """
    # Since I'm on a time crunch, I'll just meet the requirements for the
    # first sprint and nothing special. I'll expand on it later on.
    # Just the average quiz submission for now.

    # Introduction

    user_name = input("What's your name? ")
    # included a \n in the end argument in order to print on a new line
    print("Hello, ", user_name, sep='', end='!\n')
    print("This program will process your input to produce different outputs!")

    # String operators

    string1 = input("Type a phrase: ")
    string2 = input("Type another:  ")
    multiplier = int(
        float(input("Type the amount of times to repeat these phrases: ")))
    # concatenates the two strings, and prints the result the amount of
    # times the user specified
    print((string1 + string2) * multiplier)

    # Math and numeric operators

    num1 = int(float(input("type a value for a ")))
    num2 = int(float(input("type a value for b ")))
    # the - sign is the subtraction operator
    print("a - b =                           ", format(num1 - num2, '20.0f'),
          sep='')
    # the + sign is the addition operator, when not dealing with strings
    print("a + b =                           ", format(num1 + num2, '20.0f'),
          sep='')
    # the // symbol is the floor division operator, which drops the decimal
    # of a quotient of two numbers
    print("a floor divided by b =            ", format(num1 // num2, '20.0f'),
          sep='')
    # the % symbol is the modulus operator, which finds the remainder of a
    # quotient of two numbers
    print("the remainder of a divided by b = ", format(num1 % num2, '20.0f'),
          sep='')
    # the / symbol is the division operator
    print("a divided by b =                  ", format(num1 / num2, '20.0f'),
          sep='')
    # the * symbol is the multiplication operator
    print("a times b =                       ", format(num1 * num2, '20.0f'),
          sep='')
    # the ** symbol is the exponential indication operator, which can be
    # compared to the ^ symbol.
    print("a to the power of b =             ", format(num1 ** num2, '20.0f'),
          sep='')

    print("This program is 50 lines of code. Sort of.")


def main():
    game = Game()

    execute_code_from_sprint1()
    input(
        "Now begins the prototype for the final project. "
        "Everything prior was just from Sprint 1. Press Enter to play. "
        "WASD to move around.")  # using input() to stop the auto printing

    game.update_screen()  # generates first frame before input is taken in
    game_is_running = True
    while game_is_running:
        player_direction = ""  # clears the variable for the next loop
        # Handle Input
        current_command = str(msvcrt.getwch())

        # print(current_command)
        if current_command == constants.QUIT_COMMAND:
            exit()
        elif current_command == constants.MOVE_LEFT_COMMAND:
            player_direction = "left"
        elif current_command == constants.MOVE_RIGHT_COMMAND:
            player_direction = "right"
        elif current_command == constants.MOVE_UP_COMMAND:
            player_direction = "up"
        elif current_command == constants.MOVE_DOWN_COMMAND:
            player_direction = "down"

        game.player.move(player_direction)
        game.update_screen()

        if game.player.check_collision(game.orc[0]):
            game_is_running = False


if __name__ == "__main__":
    main()
