from pickle import TRUE
import string
import random

    #I am first creating Variables for my Breakfast, Lunch, Dinner and Dessert list
Breakfast_List = ('Eggs', 'Cereal', 'Waffles', 'Oatmeal')
Lunch_List = ('Burrito', ' Pizza', ' Tacos', ' PadThai')
Dinner_List = ('Steak&Potatoes',  ' Pizza',  ' TacoSalad',  ' StirFry')
Dessert_List = ('IceCream', ' Cake',  ' Cookies',  ' ApplePie')

    #Random Choice variables for Breakfast, Lunch, Dinner and Dessert
computer_actions_1 = random.choice(Breakfast_List)
computer_actions_2 = random.choice(Lunch_List)
computer_action_3 = random.choice(Dinner_List)
computer_actions_4 = random.choice(Dessert_List)

    #Setting up User Action Input to Pick Breakfast, Lunch, Dinner, or Dessert
user_action_1 = input('What Would you Like? Breakfast, Lunch, Dinner or Dessert?\n')


    #This is the input if the User goes with Breakfast
if user_action_1 == "Breakfast":
    print('Here are your Options for Breakfast')
    print(Breakfast_List)
if user_action_1 == "breakfast":
    print('Here are your Options for Breakfast')
    print(Breakfast_List)

    #This is the input if the User goes with Lunch
if user_action_1 == "Lunch":
    print('Here are your Options for Lunch')
    print(Lunch_List)
if user_action_1 == "lunch":
    print('Here are your Options for Lunch')
    print(Lunch_List)

    #This is the input if the User goes with Dinner
if user_action_1 == "Dinner":
    print('Here are your Options for Dinner')
    print(Dinner_List) 
if user_action_1 == "dinner":
    print('Here are your Options for Dinner')
    print(Dinner_List)

    #This is the input for if the User goes with Dessert
if user_action_1 == "Dessert":
    print('Here are your Options for Dessert')
    print (Dessert_List)
if user_action_1 == "dessert":
     print('Here are your Options for Dessert')
     print(Dessert_List)
    

user_action_2 = input("Would You Like Me to Choose for You?\n")

if user_action_1 == "Breakfast":
    print(computer_actions_1)
if user_action_1 == "Lunch":
    print(computer_actions_2)
if user_action_1 == "Dinner":
    print(computer_action_3)
if user_action_1 == "Dessert":
    print(computer_actions_4)




   
