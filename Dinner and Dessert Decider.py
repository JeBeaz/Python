from pickle import TRUE
import string
import random

#I am first creating Variables for my Dinner and Dessert list
Dinner_List = ('Steak&Potatoes', ' Pizza', ' TacoSalad', ' StirFry')
Dessert_List = ('IceCream', ' Cake', ' Cookies', ' ApplePie')

    #Setting up User Action & Random Computer Action to Decide Dinner or Dessert
user_action = input('What Would you Like? Dinner or Dessert?\n')
computer_action = random.choice(Dinner_List)
computer_actions = random.choice(Dessert_List)

#This is the input if the User goes with Dinner
if user_action == "Dinner":
    print('Here are your Options for Dinner')
    print(Dinner_List) 

    user_action = input('Would you Like Me To Pick One For You?\n')
    if user_action == "Yes":
        print(computer_action)
    if user_action == "No":
        print("Okay, Goodbye")

#This is the input for if the User goes with Dessert
if user_action == "Dessert":
        print('Here are your Options for Dessert')
        print (Dessert_List)

        user_actions = input('Would you Like Me To Pick One For You?\n')
        if user_actions == "Yes":
            print(computer_actions)
        if user_actions == "No":
            print('Okay, Goodbye')
