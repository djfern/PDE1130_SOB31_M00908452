import random

def compare_numbers(number, user_guess):
    ## your code here
    cow=0 #declared it to 0 so we can add it as a counter variable in the loop, to return the wrong guesses
    bull=0 #declared it to 0 so we can add it as a counter variable in the loop, to return the correct guesses
    for x in range(4): #loop to go through each digit
        if user_guess[x] == number[x]: # condition for correct digit guesses
            bull = bull + 1
        else: # condition for wronge digit guesses
            cow = cow + 1
    cowbull =[cow, bull]  #store these values to a list so that they can futher be accessed by its index position     
    return cowbull

playing = True #gotta play the game
number = str(random.randint(1000,9999)) #random 4 digit number starts from 1000
guesses = 0
print(number)

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
