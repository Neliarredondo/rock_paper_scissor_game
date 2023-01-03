# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
number_of_game = 0
user_point = 0
computer_point = 0
amount = int(input("how many game do you want to play? "))

while number_of_game < amount:
    

    #use input to ask the user for their choice 
    print("-------------------------------------------")
    user_selection = str(input("ingresa tu seleccion: "))
    print("tu eleccion es: ", user_selection)

    #create a list with rock, paper and scissor 
    opciones = ["rock", "paper", "scissor"]

    #seleccion del computador 
    import random 
    computer_selection = random.choice(opciones)
    print("la eleccion de la computadora es: ", computer_selection)

    #game logic
    if (user_selection == "rock") and (computer_selection == "paper"):
        computer_point = computer_point + 1
        print("the user lost")
    if (user_selection == "rock") and (computer_selection == "scissor"):
        print("the user win")
        user_point = user_point + 1 
    if (user_selection == "rock") and (computer_selection == "rock"):
        print("no one, try again!")
    elif (user_selection == "scissor") and (computer_selection == "paper"):
        print("the user win")
        user_point = user_point + 1 
    if (user_selection == "scissor") and (computer_selection == "rock"):
        print("the user lost")
        computer_point = computer_point + 1
    if (user_selection == "scissor") and (computer_selection == "scissor"):
        print("no one, try again!")
    elif (user_selection =="paper") and (computer_selection == "scissor"):
        print("the user lost")
        computer_point = computer_point + 1
    if (user_selection == "paper") and (computer_selection == "rock"):
        print("the user win")
        user_point = user_point + 1 
    if (user_selection == "paper") and (computer_selection == "paper"):
        print("no one, try again!")
    
        
    number_of_game = number_of_game+1
    
print("-----------------------------------")
print(f"computer point is: {computer_point}")
print(f"user point is: {user_point}")
    
