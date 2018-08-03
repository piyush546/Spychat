# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 02:37:07 2018

@author: pc
"""
# Written by Piyush Kumar
# A project for building an terminal based spychat app
# Following PEP Guidlines and Zen of Python

# To import default user data
from spy_details import spy, Spy, friends, Chat_message

# To use Steganography method
from stegano import lsb

# To get colored text output
from termcolor import colored

# Welcome message
# Strings to be wriiten in either single quotes or double quotes
# For convenience I am using double quotes
# center is used to print the strings in the center
print(colored("Spychat Terminal".center(50, "-"), 'white', 'on_grey'))

# Welcome message
print(colored("Hello", 'yellow'))

# In case of single quotes 'let\'s get started'
print("Lets's get started")

# Existing status list
Status_messages = ['Mission impossible', 'Mission X', 'Adios']


# 1.Function for adding status
def add_status(status):

    print(f'Your current status is {status}')
    status_choice = int(input("What do you want to do for your status?"\
                              "\n1. Select from older status"\
                              "\n2. Create a new status update\n"))
    if status_choice == 1:
        for a in Status_messages:
            print(f'{Status_messages.index(a)+1}. {a}')
        oldstatus_choice = int(input("Enter the status you want to update:"))
        status = Status_messages[oldstatus_choice-1]

    elif status_choice == 2:
        new_status = input("Enter your new status you want to update:")
        if len(new_status) > 0:
            Status_messages.append(new_status)
            status = new_status
        else:
            print("Invalid status")

    return status


# 2.Function for adding friends
def add_friend():

    friend_obj = Spy(" ", " ", 0, 0.0)

    friend_obj.name = input("Enter your friend name:")

    # Validating the name
    if friend_obj.name.isspace is True or len(friend_obj.name) == 0:
        print("Enter a valid name")

    else:
        # To capitalize the first character of a string
        friend_obj.name = friend_obj.name.capitalize()

        friend_obj.salutation = input("What do you want to use"\
                                      " with your friend name Dr./Mr./Mrs?\n")
        friend_obj.salutation = friend_obj.salutation.capitalize()

        # Updating the values of the variable
        friend_obj.name = f'{friend_obj.salutation} {friend_obj.name}'

        friend_obj.age = int(input("Enter the Spy age:"))
        if 12 < friend_obj.age < 50:
            friend_obj.ratings = float(input("Enter the spy Ratings"\
                                             " for your friend:"))

            if friend_obj.ratings >= 4.5 or 3.5 <= friend_obj.ratings < 4.5:
                friends.append(friend_obj)
            else:
                print("Enter a valid rating")

        else:
            print("You are not eligible for being a spy")

    # To return the numbers of friends user have
    return len(friends)


# Function for selecting a friend to chat with
def select_a_friend():

    # Iterating in the list of friends objects of the class
    for friend in friends:
        print(f'{friends.index(friend)+1}. {friend.name}'\
              f' with age: {friend.age} and ratings: {friend.ratings}')

    # Asking the user to
    chat_choice = int(input("Enter the friend with whom you want to chat:"))
    chat_choice = chat_choice - 1

    if chat_choice + 1 > len(friends):
        print("Sorry! You have entered a choice out of the range")
    else:
        return chat_choice


# 3.Function for sending message to a friend
def send_a_message():

    # Select a friend to chat with
    friend_choice = select_a_friend()

    # Adding the image you want to encrypt
    image_name = input("Enter the name of the image you want to send:")

    # Adding the message you want to hide with the pic
    secret_message = input("Enter the message you want to hide with image:")

    # The image path name after encryption
    output_path = 'output.png'

    # Encrpyting the message with the image using steganography technique
    encrypt = lsb.hide(image_name, secret_message)
    encrypt.save(output_path)

    # Calling the chat class for saving the message
    chat_obj = Chat_message(secret_message, True)

    # Add the message along with the friend name
    friends[friend_choice].chats.append(chat_obj)
    print("Your secret message is ready!")


# Defining a function for sending a special words in the message
def send_message_help():

    # select a friend who have sent the emergency message
    friend_choice_1 = select_a_friend()

    # The help message
    text = "I am coming for help"

    # The message will be added in the chat
    chat_obj = Chat_message(text, True)
    # Add the message to one who said
    friends[friend_choice_1].chats.append(chat_obj)


# 4.Function for reading secret message sent by the user
def read_a_message():

    # Select a friend to communicate with
    sender = select_a_friend()

    # Exception handling in case no message in the image
    try:
        # To input the path of enccrypted image
        image_to_decode = input("Enter the image to be decoded:")

        # decoded message
        decoded_message = lsb.reveal(image_to_decode)

    except TypeError:
        print(colored("Sorry! there is no message to decode with the image"), 'red')

    else:
        # To maintain the length of the message send by sender everytime
        words = decoded_message.split()
        new = (decoded_message.upper()).split()
        friends[sender].count += len(words)

        # Checking for some special message using membership operator
        if 'SOS' in new or 'SAVE ME'in new:
            print(colored("ATTENTION REQUIRED ".center(50, "!"), 'red'))
            print("Your friend who send the message needs help")
            print("Send him a confirmation message for help")
            # Calling help message function
            send_message_help()

            print("Move ahead! Your help message has been send")
            # To add the message with sender
            chat_obj_2 = Chat_message(decoded_message, False)
            friends[sender].chats.append(chat_obj_2)
        else:
            # To add the message with sender
            chat_obj_2 = Chat_message(decoded_message, False)
            friends[sender].chats.append(chat_obj_2)
        print("Your secret message has been decoded!")

        # Printing average word spoken by your friend
        print(f'Average word spoken by {friends[sender].name} is'\
              f'{friends[sender].count}')
        # Removing a spy who is speaking too much
        if len(words) > 100:
            print(f'Remove this chatterbox spy {friends[sender].name}')
            friends.remove(friends[sender])


# 5.Function to read chat history
def read_chat_history():

    # To select which friend is to be communicated
    read_for = select_a_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            # date and time printed in blue
            print(colored(f'{chat.time}', 'blue'))
            # name printed in red
            print(colored("You said", 'red'))
            # messages printed in black
            print(f'{chat.message}')
        else:
            # date and time printed in blue
            print(colored(f'{chat.time}', 'blue'))
            # name printed in red
            print(colored(f'{friends[read_for].name} said', 'red'))
            # messages printed in black
            print(f'{chat.message}')


# Function to print final welcome message and present the available choices
def start_chat(spy):
    # Updating user name
    # f-string literal - Introduced in Python 3.6 for conactenating the strings
    spy.name = f'{spy.salutation} {spy.name}'

    # Final welcome message
    print(f'Authentication Completed! Welcome {spy.name} '\
          f'age: {spy.age} rating: {spy.ratings}')

    # Showing the available choices
    spy_choice = True
    while spy_choice:
        # Printing the choices for a spy to choose
        spy_choose = int(input(("MENU".center(50, "*")+"\n"\
                                "1. Add a status update\n"\
                                "2. Add a friend\n"\
                                "3. Send a secret message\n"\
                                "4. Read a secret message\n"\
                                "5. Read chats from user\n"\
                                "6. Close application\n")))
        if spy_choose == 1:
            spy.status = add_status(spy.status)
            print(f'Your updated status is {spy.status}')

        elif spy_choose == 2:
            spy_friendcount = add_friend()
            print(f'Total number of friend you have is: {spy_friendcount}')

        elif spy_choose == 3:
            send_a_message()

        elif spy_choose == 4:
            read_a_message()

        elif spy_choose == 5:
            read_chat_history()

        elif spy_choose == 6:
            spy_choice = False

        else:
            print("Please enter a valid choice")


# Asking user choice whether default or custom
# Type casting - converting one format to another like string to int
# Python by defaultt take input in string
choice = int(input("How would you like to continue?"\
                    "\n1. Default user\n"\
                    "2. Custom user\n"))

# Control flow( condition + action )
# Conditional statement if. elif, else
if choice == 1:

    print("Okay")

    # Function call
    start_chat(spy)

elif choice == 2:
    # Initializing the spy class to input new data for the user
    spy = Spy(" ", " ", 0, 0.0)

    spy.name = input("Enter the Spy name:")

    # Validating the name
    if spy.name.isspace is True or len(spy.name) == 0:
        print("Enter a valid name")

    else:
        # Capitalizing the first character of the name entered by user
        spy.name = spy.name.capitalize()

        spy.salutation = input("What do you want to use with your name"\
                               " Dr./Mr./Mrs?\n")
        spy.salutation = spy.salutation.capitalize()

        spy.age = int(input("Enter the Spy age:"))
        # Validating the age and ratings entered by user
        if 12 < spy.age < 50:

            spy.ratings = float(input("Enter the spy Ratings:"))

            if spy.ratings >= 4.5:
                print("Great Ace")
            elif 3.5 <= spy.ratings < 4.5:
                print("Better one")
            else:
                print("Enter a valid rating")

            # Setting the user online
            spy.is_online = True

            start_chat(spy)
        else:
            print("You are not eligible for being a spy")
            exit()
else:
    print("Sorry!You have entered an invalid choice")
    print("You have to run this program again")
