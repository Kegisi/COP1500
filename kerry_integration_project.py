# Dennis Kerry 
# Professor Osheroff
# COP 1500
# February 2023 Spring

import msvcrt

def stuffFromSprint1():
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
    multiplier = int(float(input("Type the amount of times to repeat these phrases: "))) 
    # concatonates the two strings, and prints the result the amount of times the user specified
    print((string1 + string2) * multiplier)


    # Math and numeric operators

    num1 = int(float(input("type a value for a ")))
    num2 = int(float(input("type a value for b ")))
    #the - sign is the subtraction operator
    print("a - b =                           ", format(num1 - num2, '20.0f'), sep='')
    #the + sign is the addition operator, when not dealing with strings
    print("a + b =                           ", format(num1 + num2, '20.0f'), sep='')
    #the // symbol is the floor division operator, which drops the decimal of a quotient
    #of two numbers
    print("a floor divided by b =            ", format(num1 // num2, '20.0f'), sep='')
    #the % symbol is the modulus operator, which finds the remainder of a quotient
    #of two numbers
    print("the remainder of a divided by b = ", format(num1 % num2, '20.0f'), sep='')
    #the / symbol is the division operator
    print("a divided by b =                  ", format(num1 / num2, '20.0f'), sep='')
    #the * symbol is the multiplication operator
    print("a times b =                       ", format(num1 * num2, '20.0f'), sep='')
    #the ** symbol is the exponential indication operator, which can be compared
    #to the ^ symbol.
    print("a to the power of b =             ", format(num1 ** num2, '20.0f'), sep='')

    print("This program is 50 lines of code. Sort of.")


game_is_running = True

WINDOW_WIDTH = 24
WINDOW_HEIGHT = 12

MOVE_LEFT_COMMAND = "b'a'"
MOVE_RIGHT_COMMAND = "b'd'"
MOVE_UP_COMMAND = "b'w'"
MOVE_DOWN_COMMAND = "b's'"
QUIT_COMMAND = "b'q'"

AMOUNT_OF_ORCS = 3

turn_counter = 0


def updateScreen():
    # The play area is printed using periods for each space (temporary for visualizing)
    orc_should_be_here = False
    for current_y_pos in range(WINDOW_HEIGHT):
        for current_x_pos in range(WINDOW_WIDTH):
            # For each orc, print o
            for current_orc in range(AMOUNT_OF_ORCS):
                if ((current_x_pos + 1) == orc[current_orc].x) and ((current_y_pos + 1) == orc[current_orc].y):
                    orc_should_be_here = True

            # This line of code will print @ where the current player coords are
            if ((current_x_pos + 1) == player.x) and ((current_y_pos + 1) == player.y):
                print('@', end=' ')
                orc_should_be_here = False
            elif orc_should_be_here:
                print('o', end=' ')
                orc_should_be_here = False
            else:
                print(' ', end=' ')
        print()


def moveObject(direction, object_x, object_y):
    if direction == "left":
        object_x -= 1
    elif direction == "right":
        object_x += 1
    elif direction == "up":
        object_y -= 1
    elif direction == "down":
        object_y += 1
    
    # make sure the object does not move beyond the borders of the window
    if object_x <= 0:
        object_x = 1 
    elif object_x > WINDOW_WIDTH:
        object_x = WINDOW_WIDTH
    elif object_y <= 0:
        object_y = 1
    elif object_y > WINDOW_HEIGHT:
        object_y = WINDOW_HEIGHT
        
    return(object_x, object_y)


def checkNear(object1, object2):
    if abs(object1.x - object2.x) == 1 and abs(object1.y - object2.y) == 1:
        return True
    else:
        return False


def checkCollision(object1, object2):
    if object1.x == object2.x and object2.x == object2.y:
        return True
    else:
        return False

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Orc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# The floor divisions will set the player's starting position in the center of the screen
player = Player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

orc = [Orc(2,3), Orc(4,5), Orc(6,8)]


stuffFromSprint1()

# Only using input() to temporarily stop the autoprintinig
input("Now begins the prototype for the final project. Everything prior was just from Sprint 1. Press Enter to play. WASD to move around.")

updateScreen()
print("Turn:", format(turn_counter,str(WINDOW_WIDTH*2 - 7)+'.0f'))

# The Game Loop will keep running and repeatedly take in player commands
while game_is_running:
    ### Handle Input ###
    # msvcrt.getwch is a method that returns what the user typed in the command line before they hit enter
    current_command = str(msvcrt.getch())
    player_direction = ""

    #print(current_command)
    if current_command == QUIT_COMMAND:
        game_is_running = False
    elif current_command == MOVE_LEFT_COMMAND:
        player_direction = "left"
    elif current_command == MOVE_RIGHT_COMMAND:
        player_direction = "right"
    elif current_command == MOVE_UP_COMMAND:
        player_direction = "up"
    elif current_command == MOVE_DOWN_COMMAND:
        player_direction = "down"
    
    # used a Tuple assignment to update the player position based on input
    player.x, player.y = moveObject(player_direction, player.x, player.y)
    updateScreen()
    turn_counter +=1
    print("Turn:", format(turn_counter,str(WINDOW_WIDTH*2 - 7)+'.0f'))

    if checkCollision(player, orc[0]):
        game_is_running = False

