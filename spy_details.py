# Importing datetime to display the chat time and date
from datetime import datetime

# made a class for spy
class Spy:

    def __init__(self, name, salutation, age, rating):
        # Initialising the information
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        # Confirm that the spy is online
        self.is_online = True
        # Creates a new empty list
        self.chats = []
        self.current_status_message = None
        # Count the number of words
        self.count = 0

# a class for chat_messages
class ChatMessage:
    def __init__(self, message):
        self.message = message
        self.time = datetime.now()
        
# Defaut user:
spy = Spy('Angelina', 'Ms', 20, 4)

# Friends:
friend_one = Spy('Mark', 'Mr', 27, 4.1)
friend_two = Spy('Justin', 'Mr', 21, 4.2)
friend_three = Spy('Logan', 'Ms', 27 , 4.3)

# List of friends
friends = [friend_one, friend_two, friend_three]
