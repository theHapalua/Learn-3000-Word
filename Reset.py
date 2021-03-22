import os
file = open(".Words.txt","r")
Words = file.readlines()
file.close()
file = open("Words.txt","w")
file.writelines(Words)
file.close()
file = open("Learnings.txt","w")
file.close()
