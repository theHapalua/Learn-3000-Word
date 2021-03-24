import sys
sys.path.append("module")
from prints import *

import random

file = open("texts/Words.txt","r")
Words = file.readlines()
file.close()
file = open("texts/Learnings.txt","a")
RandomIndex = random.randint(0,len(Words))
theWord = Words.pop(RandomIndex)
outputMessage(theWord)
softwareMessage("Do you want to add this word to your Learning file? (y or n) : ")
LearningChoose = input("")
if LearningChoose == "y":
    file.write(theWord+"\n")
    file.close()
    file = open("texts/Words.txt","w")
    file.writelines(Words)
    file.close()
    softwareMessage("Successfully added to Learning file")
elif LearningChoose == "n":
    file.close()
    softwareMessage("Word didn\'t added")
else:
    errorMessage("An error occured")
