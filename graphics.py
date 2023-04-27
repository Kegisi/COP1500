import os


def hide_cursor():
    print('\033[?25l')


def show_cursor():
    print('\033[?25h')


def clear():
    print('\033[0;0H')


def main():
    """Sets the terminal window to understand ansii codes"""
    os.system('')


main()
