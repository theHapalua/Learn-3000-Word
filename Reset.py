import sys
sys.path.append("module")
from prints import *

import os
file = open("texts/AllWords.txt","r")
Words = file.readlines()
file.close()
file = open("texts/Words.txt","w")
file.writelines(Words)
file.close()
file = open("texts/Learnings.txt","w")
file.close()
