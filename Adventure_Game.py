import time
import random
import sys
from os import system, name


def print_with_delay(statement_to_print):
    '''
    Takes a statement and prints it with delay.

    Args:
        statement_to_print (string): The statement to print.
    
    Returns:
        The statement displayed with delay.
    '''

    print(statement_to_print)
    time.sleep(2)


def scenario1(scenario1_statements):
    '''
    Prints the statements of the first defeat scenario.
    
    Args:
        scenario1_statements (list): The statements of the first defeat scenario.
    
    Returns:
        The list of the statements of the first defeat scenario.
    '''

    print_with_delay(scenario1_statements)


def scenario2(scenario2_statements):
    '''
    Prints the statements of the second defeat scenario.
    
    Args:
        scenario2_statements (list): The statements of the second defeat scenario.
    
    Returns:
        The list of the statements of the second defeat scenario.
    '''
    
    print_with_delay(scenario2_statements)

starting_statements = [
    "\nYou find yourself standing in the corner, under a light post.",
    "There is a door just across the street.",
    "You are there waiting for hours.",
    "Suddenly, the door opens and an ugly tall guy makes his appearance.",
    "Your first reaction is to go directly to him but then you see better.",
    "He has a gun at his right hand while he drags a young girl with him.\n",
    "Enter 1 if you are brave enough to try your luck with him.",
    "Enter 2 to stay hidden.\n",
    "What do you want you do?"]

scenario1_statements = [
    "You attack the guy with your bare hands.",
    "Unfortunately, he's much stronger than you.",
    "Plus, he knows karate.",
    "He throws you with force down to the street.\n"]

scenario2_statements = [
    "You run to your car.",
    "You pick up your gun and use your phone to call 911.",
    "You then go back to confront the abuser.\n"]

game_over_statements1 = [
    "Your effort was desperate & reckless.",
    "The bad guy killed you.",
    "Plus, he took the poor girl with him.\n"]

game_over_statements2 = [
    "Okay, you totally messed it up.",
    "This was the worst decision you ever made.",
    "You really have to act less recklessly next time.",
    "At least, you didn't lose your life.\n"]

game_over_statements3 = [
    "The guy got away.",
    "The police came very late.",
    "You were lucky, but the girl didn't make it.\n"]


def game_end1(game_over_statements1):
    '''
    Prints the statements of the first possible game over case.
    
    Args:
        game_over_statements1 (list): The statements of the first possible game over case.
    
    Returns:
        The list of the statements of the first possible game over case.    
    '''

    for statement in game_over_statements1:
        print_with_delay(statement)


def game_end2(game_over_statements2):
    '''
    Prints the statements of the second possible game over case.
    
    Args:
        game_over_statements1 (list): The statements of the second possible game over case.
    
    Returns:
        The list of the statements of the second possible game over case.
    '''

    for statement in game_over_statements2:
        print_with_delay(statement)


def game_end3(game_over_statements3):
    '''
    Prints the statements of the third possible game over case.
    
    Args:
        game_over_statements1 (list): The statements of the third possible game over case.
    
    Returns:
        The list of the statements of the third possible game over case.
    '''

    for statement in game_over_statements3:
        print_with_delay(statement)


def end_with_defeat():
    '''
    Prints the "Game Over" sign when the player loses.
    It is printed after displaying of game_over_statements.

    Args:
        -
    
    Returns:
        The "Game Over" sign, displayed on the screen as if it is written in a typewriter.
    '''
    
    print_like_typewriter("=========\n")
    print_like_typewriter("GAME OVER\n")
    print_like_typewriter("=========\n")


def random_defeat_scenario():
    '''
    When the player makes a bad choice at the beginning and therefore loses,
    the defeat scenario is decided in a random way.
    This is only a way to fullfill the requirement to have a result that
    comes from player's choice but also an element of randomness in the plot.

    Args:
        -
    Returns:
        The statements of the randomly chosen defeat scenario.
    '''

    x = random.randint(1, 3)
    if x == 1:
        game_end1(game_over_statements1)
    elif x == 2:
        game_end2(game_over_statements2)
    elif x == 3:
        game_end3(game_over_statements3)
    end_with_defeat()


win_statements1 = [
    "Wow, you totally nailed it!",
    "The bad guy was arrested.",
    "Plus, the girl was saved.\n"]

win_statements2 = [
    "The girl was saved unharmed.",
    "You killed the bad guy,",
    "but he had a partner that fled unnoticed.\n"]

win_statements3 = [
    "A policeman patrol happened to pass by,",
    "and they arrested the guy. You were very lucky!",
    "Both you & the girl escaped without a scratch.\n"]


def win1(win_statements1):
    '''
    Prints the statements of the first winning scenario.
    
    Args:
        win_statements1 (list): The statements of the first winning scenario.
    
    Returns:
        The list of the statements of the first winning scenario.
    '''

    for statement in win_statements2:
        print_with_delay(statement)


def win2(win_statements2):
    '''
    Prints the statements of the second winning scenario 
    
    Args:
        win_statements2 (list): The statements of the second winning scenario.
    
    Returns:
        The list of the statements of the second winning scenario.
    '''

    for statement in win_statements2:
        print_with_delay(statement)


def win3(win_statements3):
    '''
    Prints the statements of the third winning scenario.
    
    Args:
        win_statements3 (list): The statements of the third winning scenario.
    
    Returns:
        The list of the statements of the third winning scenario.
    '''

    for statement in win_statements3:
        print_with_delay(statement)


def end_with_win():
    '''
    Prints the "THE END" sign when the player wins.
    It is printed after displaying of win_statements.
    
    Args:
        -
    
    Returns:
        The "THE END" sign, displayed on the screen as if it is written in a typewriter.
    '''
    print_like_typewriter("=======\n")
    print_like_typewriter("THE END\n")
    print_like_typewriter("=======\n")


def random_win_scenario():
    '''
    When the player makes a good choice at the beginning and therefore wins,
    the win scenario is decided in a random way.
    
    Args:
        -

    Returns:
        The statements of the randomly chosen winning scenario.
    '''

    x = random.randint(1, 3)
    if x == 1:
        win1(win_statements1)
    elif x == 2:
        win2(win_statements2)
    elif x == 3:
        win3(win_statements3)
    end_with_win()


def play_game():
    '''
    This is the main function of the game.
    After displaying the starting statements, the player must make
    their first and decisive choice that will define whether they win or lose.
    "decision" is a global variable so that it can be used in the next function.

    Args:
        -

    Returns:
        Starts the game.
    '''

    global decision
    for statement in starting_statements:
        print_with_delay(statement)
    while True:
        response = input("Please enter 1 or 2.\n\n")
        if response == "1":
            print_with_delay("You chose " + response + ".")
            print_with_delay("Let's see if you chose wisely.\n")
            for statement in scenario1_statements:
                scenario1(statement)
            decision = 1
            break
        elif response == "2":
            print_with_delay("You chose " + response + ".")
            print_with_delay("Let's see if you chose wisely.\n")
            for statement in scenario2_statements:
                scenario2(statement)
            decision = 2
            break
        else:
            print("Sorry, not a valid choice.\n\n")


def decide_win_or_defeat():
    '''
    It takes the global variable "decision" that comes from
    the play_game() function, decides win or defeat, and
    runs the relevant function.

    Args:
        -

    Returns:
        The statements of the random win or defeat scenario, 
        depending on whether the player won or lost.

    '''

    if decision == 1:
        random_defeat_scenario()
    elif decision == 2:
        random_win_scenario()
    else:
        print("Ops, something went wrong.")


def print_like_typewriter(the_end):
    '''
    A very primitive, special effect to make characters appear in the screen
    as if they are written in a typewriter.

    Args:
        the_end (string): "THE END", "GAME OVER" or "TO BE CONTINUED" messages.

    Returns:
        The string text displayed on screen as if it is written in a typewriter.

    '''
    
    for character in the_end:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.25)


def goodbye():
    '''
    Prints the message below when the player does not want to play again.

    Args: 
        -
    Returns:
        A message when the player does not want to play again.

    '''
    
    print_with_delay("\nHope to see you again!\n")
    print_like_typewriter("===============\n")
    print_like_typewriter("TO BE CONTINUED\n")
    print_like_typewriter("===============\n")


def start_over():
    '''
    Runs when the player decides to play again.
    
    Args:
        -
    Returns:
        -
    '''
    
    play_game()
    decide_win_or_defeat()
    ask_for_replay()


def clear(): 
    '''
    It clears the screen from the previous output in order to start fresh
    when the player decides to play again.

    Args:
        -

    Returns:
        -

    '''
    
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


def ask_for_replay():
    '''
    Runs after the end of the game. 
    The player can choose to play again or not.

    Args:
        -
    Returns:
        -
    '''
    
    while True:
        print("Do you want to play again?\n")
        response = input("Yes or No?\n").lower()
        if response == "yes":
            clear()
            start_over()
            break
        elif response == "no":
            goodbye()
            break
        else:
            print("Sorry, not a valid choice.\n\n")

play_game()
decide_win_or_defeat()
ask_for_replay()

# I was not able to make Pycodestyle work in my notebook.
# I used this page online: http://pep8online.com/ to check for any issues.
