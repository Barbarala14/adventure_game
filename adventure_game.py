import time
import random


def print_pause(seconds, message):
    print(message)
    time.sleep(seconds)


def wrong_input():
    play_again = input('Would you like to play again? (y/n)').lower()
    if play_again not in ['y', 'n']:
        print('Wrong input')
        if play_again == 'y':
            start()
        else:
            print_pause(2, 'Thanks, good bye!')
    if play_again not in ['y', 'n']:
        print('Wrong input')
        play_again = input('Would you like to play again? (y/n)').lower()
    if play_again == 'y':
        start()
    else:
        print_pause(2, 'Thanks, good bye!')

# OUTCOMES: WIN - LOSE


def win():
    script_win = ["CONGRATS, YOU WON!", "Would you like to play again? (y/n)"]
    for line in script_win:
        print_pause(2, line)
    wrong_input()


def lose():
    script_lose = "\nGAME OVER\n"
    print_pause(2, script_lose)
    play_again = input('Would you like to play again? (y/n)\n').lower()

    while play_again not in ['y', 'n']:
        play_again = input('Would you like to play again? (y/n)\n').lower()

    if play_again == 'y':
        start()
    else:
        print("Thank you for playing! See you next time!")


def random_scenarios():
    random_scripts = [
        "You drifted away and a tiger shark ate you.\n",
        "You drifted back to the shore and the crazy witch",
        "found you and kill you with a kiss.\n",
        "You drifted away to a deserted island and a group of cannibals eats"
        " you.\n"]
    choice = random.choice(random_scripts)
    print_pause(2, choice)
    lose()


def shiny_exotic_house():
    script_shiny_house = [
        "As you enter the shiny exotic beach house, the sea witch greets you."
        " While she is trying to cast a spell on you, you pull out the magic"
        " dagger that neutralises all her magic spells.",
        "\nCongratulations!!! You freed 100 enslaved men that she was hiding"
        " in her house."]
    win()


def fortress():
    script_fortress = [
        "By going into the fortress you save yourself from the tornado. "
        "And you find a golden chest. You open  the chest and take a magic "
        "dagger that was lying inside."
    ]
    for line in script_fortress:
        print_pause(2, line)

    # Stay in the fortress or leave for the beach house?
    stay_or_leave = input(
        "\nWould you like to (1) stay in the fortress or (2) go explore the"
        " shiny beach house?\n")

    while stay_or_leave not in ['1', '2']:
        print('Wrong input')
        question = 'Would you like to (1) stay in the fortress for another' \
                   ' day and rest, or (2) explore the shiny beach house?\n'
        stay_or_leave = input(question)
    if stay_or_leave == '1':
        thief = 'While you sleep, a thief enters the fortress and steals '\
                'your dagger and stabs you.'
        print_pause(2, thief)
        lose()
    else:
        shiny_exotic_house()


def escape_monster():
    script_escape_monster = [
        "By running away you managed to escape the monster and you are now"
        " back on the cliff.",
        "A tornado is forming on the sea and is coming towards the cliff where"
        " you stand."]

    for line in script_escape_monster:
        print_pause(2, line)

    fortress_or_house = input(
        "\nWould you like to (1) take shelter in the medieval fortress or (2)"
        " take shelter in the beach house?")

    while fortress_or_house not in ['1', '2']:
        print("Wrong input")
        question = "\nWould you like to (1) take shelter in the medieval" \
                   " fortress or (2) in the beach house?"
        fortress_or_house = input(question)

    # tornado kills player in beach house
    if fortress_or_house == '1':
        fortress()
    else:
        tornado_kill = "The tornado hits the shore and and wipes away the"\
                       " beach house with you inside.\n"
        print_pause(2, tornado_kill)
        lose()


def cave():
    script_cave = [
        "You approach the entrance of the sea cave.",
        "A giant sea dragon jumps out of the water.",
        "This is his kingdom and he wants to protect it by attacking you.\n"]

    for line in script_cave:
        print_pause(2, line)

    question = '\nWould you like to (1) fight it or (2) run away?\n'
    fight_or_flea = input(question)

    while fight_or_flea not in ['1', '2']:
        print('Wrong input')
        fight_or_flea = input(
            'Would you like to (1) fight it or (2) run away?')
    if fight_or_flea == '1':
        monster_kill = ['The monster is immune to arrows and you get heavily'
                        ' injured in the fight.', 'You fall unconscious into'
                        ' the water...']
        for line in monster_kill:
            print_pause(2, line)
        random_scenarios()
    else:
        escape_monster()


def house():
    script_house = ["You approach the door of the exotic beach house.", "Knock"
                    " on the door.", "A sea witch greets you and casts a spell"
                    " on you.", "You fall under her spell and she enslaves you"
                    " and traps you in her house forever.\n"]
    for line in script_house:
        print_pause(2, line)
    lose()


# GAME INTRO
def start():
    start_script = [
        "You find yourself in a green grass field on top of a cliff "
        "overlooking the ocean.\nIn your hands you hold a bow with one arrow"
        " only. In front of you there are two paths to get off the cliff.\n",
        "Which way would you like to go?",
        "(1) Go towards the cave.",
        "(2) Go towards the beach house."]
    choices = ['1', '2']
    for line in start_script:
        print_pause(2, line)
    choice = input('\n\nType 1 or 2: ')
    while choice not in choices:
        choice = input('Wrong input. Type 1 or 2:')
    if choice == '1':
        cave()
    else:
        house()


start()
