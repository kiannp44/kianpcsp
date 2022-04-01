import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
RED_COLOR = u"\u001b[34m"
TRAIN_COLOR = u"\u001b[34m"



# print a train moving across screen
def anime_print(position):
    print(ANSI_CLEAR_SCREEN)
    print(ANSI_HOME_CURSOR)
    os = " " * position
    print(RED_COLOR)
    print(os + "    ....")
    print(os + "      . . . . o o o o o")
    print(os + '              _____      o')
    print(os + "    ____====  ]OO|_n_n__][.")
    print(os + "   [________]_|__|________)<  ")
    print(os + "    oo    oo  'oo OOOO-| oo\\_ ")
    print(os + '+--+--+--+--+--+--+--+--+-+-+--+--+--+--+')

# Pattern function for animation
def animefunc():

    # Animation Variables
    start = 0  # Start with no offset
    distance = 39  # Number of loops
    step = 1  # Step amount

    # Loop in order to add animation to the train
    for position in range(start, distance, step):
        anime_print(position)
        time.sleep(.1)