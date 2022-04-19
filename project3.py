'''Mike Austin'''
'''CS Project 3'''
'''Mike Austin'''
#Import the OS module to move through dictionaries quicker
#Create the file 'scores.txt' to keep track of the name and scores
import os
#Set the menue length to a set notation
menu_length = 35
#Create the main dictionary we will be using
scores = {}


#Introduce the user to my game
print()
print("Hi, Welcome to my High Score tracker!")
#I have to define the function to get and open a file
def get_file():
    #Read the scores and sort is from highest score to lowest score
    global scores
    
    if (os.path.isfile("scores.txt")):
        with open("scores.txt", "r") as file:
            temp_file = file.read().splitlines()
            for data in temp_file:
                if (data != ""):
                    name, score = data.split(",")
                    scores[name] = int(score)
            scores =  dict(sorted(scores.items(), key=lambda item: int(item[1]), reverse = True))
    else:
        file = open("scores.txt", "x")
        file.close()
#Define and display the main menu for the user to choose from
def main_menu():
    print("-"*menu_length)
    print("1. Display high scores")
    print("2. Display all scores")
    print("3. Add/Update player score")
    print("4. Remove player score")
    print("5. Show statistics")
    print("6. Reset program and clear scores")
    print("7. Quit program")
    print("-"*menu_length)
    #Check if the user input is valid
    #Display Error messages if not valid
    user_input = input("Please choose a valid option: ")
    if (user_input.isnumeric()):
        if (int(user_input) > 0 and int(user_input) < 8):
            return int(user_input)
        else:
            print("Please enter a valid integer".upper())
            return main_menu()
    else:
        print("Please enter a valid integer".upper())
        return main_menu()
#Define and display all the highscores from scores dictionary
def display_highscores():
    #Only display the top 3 scores
    top = 3
    print("Name".center(menu_length), end="")
    print("Score".center(menu_length))
    for i,name in enumerate(scores.keys()):
        if (i == top):
            break
        print(name.center(menu_length), end="")
        print(str(scores[name]).center(menu_length))
#Define a function that will show all players and their scores
def display_all_scores():
    #Display all the scores
    print("Name".center(menu_length), end="")
    print("Score".center(menu_length))
    for name in scores.keys():
        print(name.center(menu_length), end="")
        print(str(scores[name]).center(menu_length))
#If you add a player the score the user gives
# will be appended to the dictionary scores
def add_player():
    global scores
    
    name = input("Please enter the player name: ")
    score = input("Please enter the score: ")
    if (score.isnumeric()):
        if (int(score) > 0):
            scores[name] = int(score)
            update_scores()
        else:
            print("Please enter a valid score for the player".upper())
            add_player()
    else:
        print("Please enter a valid score for the player".upper())
        add_player()
#Create a function that removes a player if their name
# is in the dictionary
def remove_player():
    #Remove the player from the scores
    global scores
    
    name = input("Please enter the players name you wish to remove: ")
    if (name in scores):
        scores.pop(name)
        update_scores()
        print()
        print("You Have Succesfully Removed {}".format(name))
        print()
    else:
        print()
        print("There is no such player".upper())
#Show the user the stats from the dictionary
def show_statistics():
    #Show number of player, average score, lowest score, highest score
    print("Number of player: {}".format(len(scores)))
    #To prevent a division by zero error, set all scores to 0
    if (len(scores) == 0):
        average_score = 0
    else:
        average_score = sum(scores.values())/len(scores)

    highest_score = 0
    lowest_score = 0
    for i, name in enumerate(scores.keys()):
        if (i == 0):
            highest_score = scores[name]
            lowest_score = scores[name]
        else:
            if (scores[name] > highest_score):
                highest_score = scores[name]

            if (scores[name] < lowest_score):
                lowest_score = scores[name]
    print("Highest score: {}".format(highest_score))
    print("Lowest score: {}".format(lowest_score))
    print("Average score: {}".format(average_score))
#Define a function to reset the program
def reset_program():
    #reset everything and clear the scores
    global scores
    scores = {}
    with open("scores.txt", "w") as file:
        file.write("")
#Update the scores
def update_scores():
    #Sort the scores and update the text file
    #If a users name is already in the dict, 
    #update the new score with that name
    global scores
    scores =  dict(sorted(scores.items(), key=lambda item: int(item[1]), reverse = True))
    
    with open("scores.txt", "w") as file:
        score_list = list(scores.items())
        for i,item in enumerate(score_list):
            score_list[i] = "{},{}".format(item[0], item[1])
        file.write("\n".join(score_list))

def main():
    #read/create file
    get_file()
    while (1):
        #Display the main menu in a loop to allow the user to continuesly choose new options
        menu_option = main_menu()
        #Based on menu option, the user wil choose an option
        if (menu_option == 1):
            display_highscores()
        
        elif (menu_option == 2):
            display_all_scores()
            
        elif (menu_option == 3):
            add_player()
            
        elif (menu_option == 4):
            remove_player()
            
        elif (menu_option == 5):
            show_statistics()
            
        elif (menu_option == 6):
            print()
            print("You Have Succesfully Cleared The Board Of All Scores!")
            print()
            reset_program()

        elif (menu_option == 7):
            print()
            print("Goodbye! Thank You For Using Me!")
            print()
            break


if __name__ == "__main__":
    main()