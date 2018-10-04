# Rock Paper Scissors 

userInput = input("Type y to continue. Press any other key to quit: ")

while (userInput == "y"):
    player1 = str(input("Player 1: Select from Rock, Paper or Scissors\n"))
    if (player1 != "Rock" and player1 != "Paper" and player1 != "Scissors"):
        print ("Invalid input")
        break 

    player2 = input("Player 2: Select from Rock, Paper or Scissors\n")
    if (player2 != "Rock" and player2 != "Paper" and player2 != "Scissors"):
        print ("Invalid input")
        break 

    if(player1 == player2): print ("There is no winner. Both players selected " +player1)
    elif (player1 == "Rock" and player2 == "Scissors"): print ("Player 1 wins")
    elif (player1 == "Scissors" and player2 == "Paper"): print ("Player 1 wins")
    elif (player1 == "Paper" and player2 == "Rock"): print ("Player 1 wins")
    else: print ("Player 2 wins")

    userInput = input("Do you wish to continue (y/n): ")