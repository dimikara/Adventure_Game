import time
import random
import sys


def print_with_delay(statement_to_print):
    print(statement_to_print)
    time.sleep(2)


def scenario1(scenario1_statements):
    print_with_delay(scenario1_statements)


def scenario2(scenario2_statements):
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
    for statement in game_over_statements1:
        print_with_delay(statement)


def game_end2(game_over_statements2):
    for statement in game_over_statements2:
        print_with_delay(statement)


def game_end3(game_over_statements3):
    for statement in game_over_statements3:
        print_with_delay(statement)


def end_with_defeat():
    print_like_typewriter("=========\n")
    print_like_typewriter("GAME OVER\n")
    print_like_typewriter("=========\n")


def random_defeat_scenario():
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
    for statement in win_statements2:
        print_with_delay(statement)


def win2(win_statements2):
    for statement in win_statements2:
        print_with_delay(statement)


def win3(win_statements3):
    for statement in win_statements3:
        print_with_delay(statement)


def end_with_win():
    print_like_typewriter("=======\n")
    print_like_typewriter("THE END\n")
    print_like_typewriter("=======\n")


def random_win_scenario():
    x = random.randint(1, 3)
    if x == 1:
        win1(win_statements1)
    elif x == 2:
        win2(win_statements2)
    elif x == 3:
        win3(win_statements3)
    end_with_win()


def play_game():
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
    if decision == 1:
        random_defeat_scenario()
    elif decision == 2:
        random_win_scenario()
    else:
        print("Ops, something went wrong.")


# https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
def print_like_typewriter(the_end):
    for character in the_end:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.25)


def goodbye():
    print_with_delay("\nHope to see you again!\n")
    print_like_typewriter("===============\n")
    print_like_typewriter("TO BE CONTINUED\n")
    print_like_typewriter("===============\n")


def start_over():
    play_game()
    decide_win_or_defeat()
    ask_for_replay()


def ask_for_replay():
    while True:
        print("Do you want to play again?\n")
        response = input("Yes or No?\n").lower()
        if response == "yes":
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
