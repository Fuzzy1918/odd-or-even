#import random
import random

# method takes 2 inputs a string that is either 'odd' or 'even' as oORe
# and an int named guess in the range 0 - 5
def oddOrEven(oORe, guess):
    
    guess = int(guess)
    # a random int is the generated for the computers guess ranging from 0 - 5
    valueRandom = random.randint(0, 5)
    # the if statement is to ensure the user enters odd or even
    if oORe == "odd" or oORe == "even":
        # this if statement is to ensure the user entered an int from the range 0 - 5
        if -1 < guess < 6:
            total = guess + valueRandom
            print("The computer guessed", valueRandom)
            print("The total is", total)
            # this if statement decides if the total of the 2 guesses is odd or even
            if total % 2 == 0:
                if oORe == "even":
                    print("total is even you are the winner")
                    # returns a 1 to signify player wins
                    return 1
                else:
                    print("total is even Computer wins")
                    # returns a -1 to signify player lost
                    return -1
            else:
                if oORe == "odd":
                    print("total is odd you are the winner")
                    # returns a 1 to signify player wins
                    return 1
                else:
                    print("total is odd Computer wins")
                    # returns a -1 to signify player lost
                    return -1
        else:
            print("you must enter a number in the range 0 through 5")

    else:
        print("you must enter 'odd' or 'even' ")


# start of main method
# asks user to input 'odd' or 'even' for their guess
value = input("Please enter odd Or even: ")
value2 = input("Please enter either a number from 0-5: ")
value2 = int(value2)
# asks user to see how many times they would like the game to loop with current guesses
x = input("Please enter how many times you would like your guess to loop: ")
x = int(x)
print("The process will now loop", x, "times")

# declaring the wins and loss variables before the for loop
wins = 0
loss = 0

for x in range(x):
    # the method will return either 1 or -1 to tell if the player has won or lost
    if oddOrEven(value, value2) == 1:
        wins = wins + 1
    else:
        loss = loss + 1
    print()
    
# prints final score to see which outcome was the most likely
print("Wins:", wins)
print("Losses:", loss)
#Nice
