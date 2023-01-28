# Adam Vosburg IT-140 Text Based Game Module 7
# 12/15/2022

import time  # Googled to add an element of suspense.  This will allow me to add a time delay between messages


def main_menu():
    # Print instructions and intro
    print('@' * 60)
    print("Welcome to the Cultist Mansion")
    print("Collect 6 items to win the game, or lose your mind to the Elder Gods!")
    print('Move commands: "go North", "go South", "go East", "go West"')
    print("Add to Inventory: get 'item name'")
    print("Type 'exit' to quit.")
    print('@' * 60)

# Creating a dictionary that lists the rooms, directions and items available for each room.
rooms = {
    'Great Hall': {'East': 'Courtyard'},
    'Courtyard': {'North': 'Drawing Room', 'East': 'Bedroom', 'West': 'Great Hall', 'South': 'Dining Room',
                  'item': 'Matchbox'},
    'Drawing Room': {'East': 'Library', 'South': 'Courtyard', 'item': 'Scroll'},
    'Library': {'West': 'Drawing Room', 'South': 'Bathroom', 'item': 'Necronomicon'},
    'Dining Room': {'North': 'Courtyard', 'East': 'Kitchen', 'item': 'Candle'},
    'Kitchen': {'East': 'Dining Room', 'North': 'Bedroom', 'item': 'Pentagram'},
    'Bedroom': {'West': 'Courtyard', 'North': 'Bathroom', 'South': 'Kitchen', 'East': 'Attic', 'item': 'Key'},
    'Bathroom': {'South': 'Bedroom', 'North': 'Library', 'item': 'Skull'},
    'Attic': {'West': 'Bedroom'},

}
# Creating a dictonary that names possible directions for reference from the rooms dict
directions = {'North', 'East', 'South', 'West'}

# Assign a defintion to the current room variable to use later for movement loop
current_room = 'Great Hall'  # starts player in the Entrance Hall

Inventory = []  # Adds an inventory

main_menu()  # This will call my main menu definition

while True:  #This begins the gameplay loop
        if current_room == 'Attic':
            if len(Inventory) >= 6:
                print('You creep into the attic and stop in horror.')
                time.sleep(4)
                print('A cultist prophet stands, covered in blood before you.')
                time.sleep(4)
                print('The items fly from your hand and arrange on a nearby altar.')
                time.sleep(4)
                print('He begins chanting and a rift in reality tears open. You try to run screaming but you are glued in place')
                time.sleep(4)
                print('However, a tentacle emerges and grasps on to him in mid chant.')
                time.sleep(4)
                print('With a pitiful scream, he is dragged into the void and it abruptly closes.')
                print('You gather your wits and see a window to climb out of.')
                time.sleep(4)
                print('You are finally free.......for now.')
                break
            else:
                print('You burst into the attic but you are stopped in your tracks.')
                print('The cultist leader has cast a spell on you.')
                print('He chants a strange verse and it begins to feel like your insides are tearing apart.')
                print('The last thing you hear is his maniacal laugh.')
                time.sleep(4)
                print('YOU')
                time.sleep(4)
                print('ARE')
                time.sleep(4)
                print('DEAD')
                time.sleep(4)
                print('Thanks for playing, try again!')
                break  # This will end the game if 6 items have not been collected
        # display current location
        print()
        print('You are in the {}.'.format(current_room))  # This block of code gives status update for each room
        print('Inventory:', Inventory)
        room_dict = rooms[current_room]
        if "item" in room_dict:  # If each room has an item in dictionary it will display only those NOT in inventory
            item = room_dict['item']
            if item not in Inventory:
                print("You see a", item)

        # get user input
        movement = input("Which way would you like to go? ").split()
        # movement
        if movement[0] == 'go':
            if movement[1] in room_dict:
                current_room = room_dict[movement[1]]

            else:
                # bad movement
                print('You cannot go that way.')

        # quit game
        elif movement[0] in ['exit', 'quit']:
            print('Thanks for playing!')
            break
        # get item
        elif movement[0] == 'get':
            if movement[1] == item:
                Inventory.append(item)
                print(item, "collected")
            else:
                print('Invalid command')
        # bad command
        else:
            print('Invalid input')
