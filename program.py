# Importing the details of the spy
from spy_details import spy, Spy, friends, ChatMessage

# Importing steganography module
from steganography.steganography import Steganography



# List of status messages
STATUS_MESSAGES = ['Having Fun', 'Sunny Day', "Busy",
                   "Feeling Lazy", "Damm it it feels good to be a gangster", "Message only"]


print("Hello!")


print ("Let\'s get started!")


Choice = raw_input("Do you want to continue as the default user-" + spy.salutation + " " + spy.name + " or create a new user? (Y/N):")




#Function to add a status
def add_status():
    
    updated_status_message = None

    
    if spy.current_status_message is not None:
        print ('Your current status message is %s \n' % spy.current_status_message)
    else:
        print ('You don\'t have any status message currently \n')

    
    default = raw_input("Do you want to select from the older status (y/n)? ")

    
    
    if default.upper() == "N":
        
        new_status_message = raw_input("What status message do you want to see?: ")

        
        if len(new_status_message) > 0:
            
            STATUS_MESSAGES.append(new_status_message)
            
            updated_status_message = new_status_message

    
    elif default.upper() == 'Y':

        
        item_position = 1

        
        for message in STATUS_MESSAGES:
            print ('%d. %s' % (item_position, message))
            item_position = item_position + 1

        
        message_selection = int(raw_input("\nChoose the index of the status: "))

        
        if len(STATUS_MESSAGES) >= message_selection:
            
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    
    else:
        print ('The option you chose is not valid! Press either Y or N.')

    
    if updated_status_message:
        print ('Your updated status message is:'),
        print(updated_status_message)

    
    else:
        print('You did not update your status message')

    
    return updated_status_message


#Function to add a friend
def add_friend():
    
    new_friend = Spy(" ", " ", 0, 0.0)
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr or Ms?: ")

    
    new_friend.age = input("Age?: ")
    
    new_friend.age = int(new_friend.age)

    
    new_friend.rating = input("Spy rating?: ")
    
    new_friend.rating = float(new_friend.rating)

    
    
    if len(new_friend.name) > 0 and new_friend.name.isdigit() == False and 12 < new_friend.age < 50 and new_friend.salutation.isalpha() == True and  new_friend.rating >= spy.rating :

        
        friends.append(new_friend)
        print('Friend Added!')
    else:
        print("Sorry, the friend cannot be a spy!")

    
    return len(friends)



#Function to select a friend
def select_a_friend():
    
    item_number = 0

    
    for friend in friends:
        print ('%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salutation, friend.name, friend.age, friend.rating))

        item_number = item_number + 1

    
    friend_choice = raw_input("Choose the index of the friend: ")
    
    friend_choice_position = int(friend_choice) - 1

    
    if friend_choice_position + 1 > len(friends):
        print("Sorry,This friend is not present.")
        exit() 

    else:
        
        return friend_choice_position




#Function to send a message
def send_a_message():
    
    friend_choice = select_a_friend()

    
    original_image = raw_input("What is the name of the image?: ")

    
    output_path = "output.jpg"
    
    text = raw_input("What do you want to say? ")

    
    Steganography.encode(original_image, output_path, text)

    
    new_chat = ChatMessage(text)

    
    friends[friend_choice].chats.append(new_chat)

    
    print("Your secret message image is ready!")



#Function to read a message
def read_a_message():
    
    sender = select_a_friend()
    output_path = raw_input("What is the name of the image file?: ")

    
    try:
        secret_text = Steganography.decode(output_path)
        print ("The secret message you read is"),
        print (secret_text)
        words = secret_text.split()
        
        new = (secret_text.upper()).split()
                
        
            
        new_chat = ChatMessage(secret_text)
        # Adds the mesaage to the list of chats
        friends[sender].chats.append(new_chat)
        print("Your secret message has been saved!")

        
    
    # If any error occurs during decoding    
    except TypeError:
        print("Nothing to decode from the image as it contains no secret message.")


#Function to read chat history
def read_chat_history():
    read_for = select_a_friend()

    print ('\n')

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            
            print(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ","),
            
            print("You said:"),
            
            print(str(chat.message))
        else:
            
            print(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ","),
        
            print(str(friends[read_for].name) + " said:"),
            
            print(str(chat.message))












#Function to select the default user
def start_chat(spy):
    
    spy.name = spy.salutation + " " + spy.name
    
    if 12 < spy.age < 50:

        
        
        print("Authentication complete.")
        print("Welcome " + str(spy.name))
        print("Your age:" + str(spy.age))
        print("Your rating:"+str(spy.rating))
        print("Bravo!Proud to have you on board.")

        
        

        show_menu = True
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n" \
                           " 2. Add a friend \n 3. Send a secret message \n " \
                           "4. Read a secret message \n 5. Read Chats from a user \n" \
                           " 6. Close Application \n"
            
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    
                    spy.current_status_message = add_status()

                elif menu_choice == 2:
                    
                    number_of_friends = add_friend()
                    print ('You have %d friends' % number_of_friends)

                elif menu_choice == 3:
                    
                    send_a_message()

                elif menu_choice == 4:
                    
                    read_a_message()

                elif menu_choice == 5:
                    
                    read_chat_history()

                elif menu_choice == 6:
                    
                    print("Successfully closed")
                    show_menu = False

                
                else:
                    print("That was a wrong choice.")
                    exit()

    else:
        
        if spy.age <= 12:
            print("Sorry, you are too young to become a spy!")
        
        elif spy.age >= 50:
            print("Sorry, you are too old to be a spy!")





#Block of code from which execution starts

if Choice.upper() == "Y":
    #Function call for default user
    start_chat(spy)

elif Choice.upper() == "N":

    spy = Spy(" ", " ", 0, 0.0)

    #
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0 and spy.name.isdigit() == False:

        spy.salutation = raw_input("What should we call you? Mr. or Ms.?")

        if len(spy.salutation) > 0:

            
            spy.age = raw_input("Please enter your age: ")

            if len(spy.age) > 0:
                
                spy.age = int(spy.age)
                
                
                if 12 <= spy.age < 50:
                    print("Welcome to Spy community")

                    
                    spy.rating = raw_input("Please enter your spy rating: ")
                    if len(spy.rating) > 0:
                        
                        spy.rating = float(spy.rating)

                        if spy.rating > 4.5:
                            print("Great Ace!")
                        elif 3.5 <= spy.rating <= 4.5:
                            print("You are one of the good ones!")
                        elif 2.5 <= spy.rating <= 3.5:
                            print("You can always do better.")
                        else:
                            print("We will get someone to help you.")

                        
                        spy.is_online = True

                        
                        start_chat(spy)

                    
                    else:
                        print ("Enter a valid spy rating")

                
                else:
                    
                    if spy.age <= 12:
                        print("Sorry, you are too young to become a spy!")
                    
                    elif spy.age >= 50:
                        print("Sorry, you are too old to be a spy!")
                    else:
                        print("Please enter a valid age")

            
            else:
                print("Please enter your age")

        
        else:
            print("Please enter a valid salutation")

    
    else:
        print("Please enter a valid name")

else:
    print(colored("You did not reply with a yes(Y) or no(N)!", 'green'))
    print(colored("Need to run the program again.", 'green'))
    exit()