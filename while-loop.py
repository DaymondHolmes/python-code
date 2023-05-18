#specify the class library, library of random
import random

#generating random number from class library
random_number = random.randint(1,100)

#Ask the user to guess the number
guess = -1 #initialize the guess to a value not equal to the random number

#control flow statment
while guess != random_number:
    #ask for uer input from the input funtion
    guess = int(input("guess a number between 1 and and 100:"))
    
    #Creat if condition checking logic from input of end user to random number genratrd.
    if guess < random_number:
        print ("Too low")
    elif guess > random_number:
        print ("Too high")
    else:
        print("Congratulations! You guess the number")