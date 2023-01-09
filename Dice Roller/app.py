import random


def rand():
    a = random .randint(1, 6)
    return a


dict = {
    1: (
        "-----------\n"
        "|         |\n"
        "|    o    |\n"
        "|         |\n"
        "-----------\n"
    ),
    2: (
        "-----------\n"
        "| o       |\n"
        "|         |\n"
        "|       o |\n"
        "-----------\n"
    ),
    3: (
        "-----------\n"
        "| o       |\n"
        "|    o    |\n"
        "|       o |\n"
        "-----------\n"
    ),
    4: (
        "-----------\n"
        "| o     o |\n"
        "|         |\n"
        "| o     o |\n"
        "-----------\n"
    ),
    5: (
        "-----------\n"
        "| o     o |\n"
        "|    o    |\n"
        "| o     o |\n"
        "-----------\n"
    ),
    6: (
        "-----------\n"
        "| o     o |\n"
        "| o     o |\n"
        "| o     o |\n"
        "-----------\n"
    ),

}

if __name__ == '__main__':
    b = 'y'
    while b == 'y':
        r = rand()
        i = dict[r]
        print(i)
        print("The Dice rolled a {}".format(r))
        b = input("do you want to roll again? y/n  :")
