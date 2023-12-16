import random


def number_of_pencils():
    print('How many pencils would you like to use:')
    while True:
        try:
            input_pencils = int(input())
            if input_pencils > 0:
                return input_pencils
            else:
                print('The number of pencils should be positive')
        except ValueError:
            print('The number of pencils should be numeric')


def starting_person():
    valid_persons = ['John', 'Jack']
    print('Who will be the first (John, Jack):')
    while True:
        input_person = input()
        if input_person not in valid_persons:
            print("Choose between 'John' and 'Jack'")
        else:
            return input_person


def play():
    pencils = number_of_pencils()
    first_person = starting_person()

    print('|' * pencils)

    while True:
        print(f"{first_person}'s turn!")
        if first_person == 'Jack':
            bot_pencils = bot_turn(pencils)
            print(bot_pencils)
            pencils -= bot_pencils
            first_person = switch_person(first_person)
            if pencils == 0:
                print(f"{first_person} won!")
                break
            else:
                print('|' * pencils)
        else:
            player_pencils = player_turn(pencils)
            pencils -= player_pencils
            first_person = switch_person(first_person)
            if pencils == 0:
                print(f"{first_person} won!")
                break
            else:
                print('|' * pencils)


def bot_turn(pencils):
    if pencils % 4 == 0:
        return 3
    elif pencils % 4 == 3:
        return 2
    elif pencils % 4 == 2:
        return 1
    else:
        if pencils == 1:
            return 1
        elif pencils == 2:
            return random.randint(1, 2)
        else:
            return random.randint(1, 3)


def player_turn(pencils):
    while True:
        try:
            input_pencils = int(input())
            if input_pencils > 0:
                if input_pencils > 3:
                    print("Possible values: '1', '2' or '3'")
                else:
                    if input_pencils > pencils:
                        print('Too many pencils were taken')
                    else:
                        return input_pencils
            else:
                print("Possible values: '1', '2' or '3'")
        except ValueError:
            print("Possible values: '1', '2' or '3'")


def switch_person(current_person):
    players = {'Jack': 'John', 'John': 'Jack'}
    return players[current_person]


def main():
    play()


main()
