# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 02:37:52 2018

@author: pc
"""

# Written by Piyush Kumar

# Importing datetime for showing chat date and time
from datetime import datetime


# A class for spy to contain its details
class Spy():
    def __init__(self, name, salutation, age, ratings):
        # Initializing variables
        self.name = name
        self.salutation = salutation
        self.age = age
        self.ratings = ratings
        self.is_online = True
        self.chats = []
        # to count the words of the message
        self.count = 0
        self.status = None


# A class to contain chats
class Chat_message():
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


# Creating object of spy class
spy = Spy('Piyush', 'Mr.', 18, 4.5)

# Creating some default freinds odsf spy
friend_1 = Spy('Carlos', 'Dr.', 20, 5)
friend_2 = Spy('Nakamura', 'Mr.', 19, 4.0)
friend_3 = Spy('Maraiah', 'Mrs.', 22, 4.8)
friends = [friend_1, friend_2, friend_3]
