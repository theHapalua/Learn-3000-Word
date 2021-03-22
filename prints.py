def softwareMessage(*text):
    """
    Prints texts from this software.
    """
    print("\x1b[38;2;255;153;51m",end="")
    for i in text:
        print(i,end="")
    print("\x1b[39m")

def errorMessage(*text):
    """
    Prints error message.
    """
    print("\x1b[48;2;204;0;0m",end="")
    for i in text:
        print(i,end="")
    print("\x1b[49m")

def outputMessage(*text):
    """
    Prints output message.
    """
    print("\x1b[38;2;0;204;102m",end="")
    for i in text:
        print(i,end="")
    print("\x1b[39m")

