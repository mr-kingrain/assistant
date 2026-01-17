from python.speak import talk
from python.setup import setuping as setup
from python.setup import check 
from python.HandleCommand import handleC as Handle_command
import threading


def speak(a):
    t = threading.Thread(target=talk, args=(a,))
    t.start()

    #this make sure that the command is threaded
    #use talk for things where it needs a pause or smth idk
 
if not check():
    talk("hello.... can i set my environment?")

    choice = input("yes/no: ")

    if choice.lower() == "yes":
        is_set = setup()  # call the function and store result
        if is_set:  # if the function returned True
            talk("already set up")
else:

    talk("what do you want me to do?")
    on = True
    while on:
        choice = input(">")
        output = Handle_command(choice)
        speak(output)
        

