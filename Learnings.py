from prints import *
file = open("Learnings.txt",'r')
Words = file.readlines()
file.close()
for Word in Words:
    CleanWord = ""
    for letter in Word:
        if letter != "\n":
            CleanWord += letter
        else:
            pass
    Words[Words.index(Word)] = CleanWord
for Word in Words:
    if Word == '':
        Words.remove(Word)
for Word in Words:
    outputMessage(Word)
softwareMessage("\nadd : add a word that file doesn\'t include\nremove : remove a word from Learnings.txt file\nexit : exit")
AddRemoveSelection = input("")
if AddRemoveSelection == "add":
    softwareMessage("Enter the Word")
    AddingWord = input("")
    Words.append(AddingWord)
elif AddRemoveSelection == "remove":
    try:
        softwareMessage("Enter the Word")
        RemovingWord = input("")
        Words.remove(RemovingWord)
    except:
        errorMessage("An error occured")
elif AddRemoveSelection == "exit":
    pass
else:
    errorMessage("An error occured")
file = open("Learnings.txt","w")
for Word in Words:
    file.write(Word+"\n")
file.close()
