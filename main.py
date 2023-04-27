"""
Integration Project
Professor Michael Osheroff
COP 1500
February 2023
"""
__author__ = "Dennis Kerry"

import msvcrt
import random
import constants as cons
import graphics as gfx


class GameEntity:
    """Any character that is within the game"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        """
        Changes the coords of the object based on a directional value
        :param direction: A string in all lowercase
        """

        if direction == cons.MOVE_LEFT_COMMAND:
            self.x -= 1
        elif direction == cons.MOVE_RIGHT_COMMAND:
            self.x += 1
        elif direction == cons.MOVE_UP_COMMAND:
            self.y -= 1
        elif direction == cons.MOVE_DOWN_COMMAND:
            self.y += 1

        # make sure the object does not move beyond the borders of the window
        if self.x <= 0:
            self.x = 1
        elif self.x > cons.WINDOW_WIDTH:
            self.x = cons.WINDOW_WIDTH
        elif self.y <= 0:
            self.y = 1
        elif self.y > cons.WINDOW_HEIGHT:
            self.y = cons.WINDOW_HEIGHT

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
    """Holds everything relating to the game itself"""

    def __init__(self):
        self.turn_counter = 0
        self.is_running = True

    def update_screen(self):
        """Prints the grid and all the characters"""
        gfx.clear()
        orc_should_be_here = False
        for current_y_pos in range(cons.WINDOW_HEIGHT):
            for current_x_pos in range(cons.WINDOW_WIDTH):
                # For each orc, print o
                for current_orc in range(len(self.orc)):
                    if ((current_x_pos + 1) == self.orc[current_orc].x) \
                            and (
                            (current_y_pos + 1) == self.orc[current_orc].y):
                        orc_should_be_here = True

                # This line of code will print @ where the current player
                # coords are
                if ((current_x_pos + 1) == self.player.x) and (
                        (current_y_pos + 1) == self.player.y):
                    print(cons.PLAYER_SYMBOL, end=' ')
                elif orc_should_be_here:
                    print(cons.ORC_SYMBOL, end=' ')
                else:
                    print('.', end=' ')
                orc_should_be_here = False
            print()
        print("Turn:", format(self.turn_counter,
                              str(cons.WINDOW_WIDTH * 2 - 7) + '.0f'))

        self.turn_counter += 1

    def quit(self):
        """
        Sets the game to no longer be running
        """
        self.is_running = False
        gfx.show_cursor()

    # Create the player and divide the window dimensions by two to center it
    player = Player(cons.WINDOW_WIDTH // 2, cons.WINDOW_HEIGHT // 2)

    # Create the orcs
    orc = []
    for orc_number in range(cons.AMOUNT_OF_ORCS):
        orc_x = random.randint(1, cons.WINDOW_WIDTH)
        orc_y = random.randint(1, cons.WINDOW_HEIGHT)
        # Re-generate coords if they're the same as the player's
        while (orc_x == player.x) and (orc_y == player.y):
            orc_x = random.randint(1, cons.WINDOW_WIDTH)
            orc_y = random.randint(1, cons.WINDOW_HEIGHT)
        # Make sure the orc isn't being spawned in the same spot as another
        for orc_index in range(len(orc)):
            while (orc_x == orc[orc_index].x) and (orc_y == orc[orc_index].y):
                orc_x = random.randint(1, cons.WINDOW_WIDTH)
                orc_y = random.randint(1, cons.WINDOW_HEIGHT)
                orc_index = -1  # next iteration of the loop will start at 0
        orc.append(Orc(orc_x, orc_y))


def get_good_num(prompt):
    """
    Keeps asking for input until the user types a numerical value
    :param prompt: The question to ask the user
    :return: The number the user typed after it is checked
    """
    good_input = False
    while not good_input:
        try:
            answer = int(float(input(prompt)))
            good_input = True
        except ValueError:
            print("Invalid input type. Must be a number")
    return answer


def execute_code_from_sprint1():
    """
    this is just a function that contains all the requirements from Sprint 1
    """

    # Introduction

    user_name = input("What's your name? ")
    # included a \n in the end argument in order to print on a new line
    print("Hello, ", user_name, sep='', end='!\n')
    print("This program will process your input to produce different outputs!")

    # String operators

    string1 = input("Type a phrase: ")
    string2 = input("Type another:  ")
    multiplier = get_good_num("Type the amount of times to repeat these "
                              "phrases: ")
    while multiplier >= 100:
        print("This number must be less than 100")
        multiplier = get_good_num("Type the amount of times to repeat these "
                                  "phrases: ")
    # concatenates the two strings, and prints the result the amount of
    # times the user specified
    print((string1 + string2) * multiplier)

    # Math and numeric operators

    num1 = get_good_num("type a numerical value for a ")
    while num1 >= 100:
        num1 = get_good_num("a must be less than 100\n"
                            "type a numerical value for a ")
    num2 = get_good_num("type a numerical value for b ")
    while num2 >= 100:
        num2 = get_good_num("b must be less than 100\n"
                            "type a numerical value for b ")
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
    print("a to the power of b =             ",
          format(num1 ** num2, '20.0f'), sep='')

    input("Press Enter to close the program")


def main():
    """Establish the main game loop where input and logic are handled"""

    game = Game()

    gfx.hide_cursor()
    game.update_screen()
    while game.is_running:
        # Get Input
        current_command = str(msvcrt.getch())
        if (current_command == cons.MOVE_UP_COMMAND) or \
                (current_command == cons.MOVE_DOWN_COMMAND) or \
                (current_command == cons.MOVE_LEFT_COMMAND) or \
                (current_command == cons.MOVE_RIGHT_COMMAND):
            game.player.move(current_command)
        if current_command == cons.QUIT_COMMAND:
            game.quit()

        for orc_index in range(len(game.orc)):
            if game.player.check_collision(game.orc[orc_index]):
                game.quit()

        game.update_screen()

    print("Game Over!")
    execute_code_from_sprint1()


if __name__ == "__main__":
    main()
