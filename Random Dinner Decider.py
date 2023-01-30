from pickle import TRUE
import string
import random

while True:
    print("What Do You Want To Eat?")
    Dinner_List = ("StirFry", "TacoSalad", "Burgers with", "Curry", "Steak with", "Wings with","Chicken with")
    Veggie_List = (" Brocoli", " Corn", "Carrots", " Brussel Sprouts", " Zucchini", " Asparagus")

    user_action = input('Pick a number between 1 - 5:')
    possible_actions = ("Burgers with", "Steak with", "Wings with", "Chicken with",)
    computer_actions = random.choice(Dinner_List)
    computer_action = random.choice(Veggie_List)

    print(computer_actions)

    if computer_actions == "Burgers with": 
        print(computer_action)
    
    if computer_actions == "Steak with": 
        print(computer_action)
        
    if computer_actions == "Wings with": 
        print(computer_action)

    if computer_actions == "Chicken with": 
        print(computer_action)
    
    Choose_Again = input('Choose Again? (y/n)')
    if Choose_Again.lower() != "y":
        break


