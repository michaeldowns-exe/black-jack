import p1_random as p1

# print_menu function prints menu when called
def print_menu():
    print()
    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit")
    print()


def main():
    #creates variables needed for program, use p1.random function imprted from p1_random
    rng = p1.P1Random()
    counter = 0
    play = 0
    dealerNumber = 0
    gameStop = 0
    cardValue = 0
    cardName = ""
    menuInput = "1"
    gameEnd = 0
    tieGames = 0
    playerWins = 0
    dealerWins = 0

    #gameStop continues game run until menuInput == 4
    while gameStop == 0:
        counter = counter + 1
        print("START GAME #", end="")
        print(counter)
        cardValue = 0
        gameEnd = 0
        #gameEnd loop ends when user wins or loses, starts new game
        while gameEnd == 0:
            currentHand = rng.next_int(13) + 1
            if currentHand == 1:
                cardName = "ACE"
                cardValue = cardValue + 1
            elif currentHand == 11:
                cardName = "JACK"
                cardValue = cardValue + 10
            elif currentHand == 12:
                cardName =  "QUEEN"
                cardValue = cardValue + 10
            elif currentHand == 13:
                cardName = "KING"
                cardValue = cardValue + 10
            else:
                cardName = str(currentHand)
                cardValue = cardValue + currentHand
            #pulls random card, prints name of card and adds value to hand   
            print()
            print("Your card is a", cardName,end="!")
            print()
            print("Your hand is:", cardValue)
            if cardValue == 21:
                print()
                print("BLACK JACK! You win!")
                print()
                play = 1
                gameEnd = 1
                playerWins = playerWins + 1
            elif cardValue > 21:
                print()
                print("You exceeded 21! You lose.")
                print()
                play = 1
                gameEnd = 1
                dealerWins = dealerWins + 1
            else: 
                play = 0
            #play loop while user has not won or lost, win or lose bypasses menu selection and restarts game
            while play == 0:
                print_menu()
                menuInput = input("Choose an option: ")
                if menuInput != "1" and menuInput != "2" and menuInput != "3" and menuInput != "4":
                    print()
                    print("Invalid input!")
                    print("Please enter an integer value between 1 and 4.")
                else:
                    if menuInput == "1":
                        #jumps up to gameEnd loop to pull another random card
                        play = 1
                    elif menuInput == "2":
                        #pulls card number for dealer, compares, and determines win and loss
                        dealerNumber = rng.next_int(11) + 16
                        print()
                        print("Dealer's hand:", dealerNumber)
                        print("Your hand is:", cardValue)
                        print()
                        #if loop covers all possible outcomes
                        if dealerNumber < cardValue:
                            print("You win!")
                            print()
                            playerWins = playerWins + 1
                            play = 1
                            gameEnd = 1
                        elif dealerNumber == cardValue:
                            print("It's a tie! No one wins!")
                            print()
                            play = 1 
                            gameEnd = 1
                            tieGames = tieGames + 1
                        elif dealerNumber > cardValue and dealerNumber < 22:
                            print("Dealer wins!")
                            print()
                            dealerWins = dealerWins + 1
                            play = 1
                            gameEnd = 1
                        elif dealerNumber > cardValue and dealerNumber > 21:
                            print("You win!")
                            print()
                            playerWins = playerWins + 1
                            play = 1
                            gameEnd = 1    
                    elif menuInput == "3":
                        #uses values collected from win/loss/ties
                        print()
                        print("Number of Player wins:", playerWins)
                        print("Number of Dealer wins:", dealerWins)
                        print("Number of tie games:", tieGames)
                        print("Total # of games played is:", counter - 1)
                        print("Percentage of Player wins:", round((playerWins/(counter-1)*100),1),end="%")
                        print()
                        # option 4 exits every loop and ends program
                    elif menuInput == "4":   
                        play = 1
                        gameEnd = 1
                        gameStop = 1

        
main()

        
