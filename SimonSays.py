import random
import os
import time

gameRunning = True
# Starting pattern length
x = 4
numList = []
# Generates a random list consisting of numbers 1-4
for i in range(0, x):
    numList.append(random.randint(1, 4))


while(gameRunning):
    
    submissionList = []

    print("Remember this sequence:")
    print(numList)
    time.sleep(5)
    print ("\n" * 100)

    # Gets player input, checks against list, and breaks if player makes a mistake
    print("Type the sequence, pressing enter after each number:")
    for i in range(0, x):
        submissionList.append(eval(input()))
        if(submissionList[i] != numList[i]):
            break

    # Checks if player has won and reacts accordingly
    if(submissionList == numList):
        print("You win!")
        numList.append(random.randint(1, 4))
        x += 1
    else:
        print("You lose!")
        gameRunning = False
