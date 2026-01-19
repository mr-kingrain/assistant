from python.speak import talk
from python.speak import tspeak as speak
from python.setup import setuping as setup
from python.setup import check 
from python.HandleCommand import handleC as Handle_command
from python.train.run_ai import txt_detect as ai_text

import threading



 
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
        with open("user_input.txt", "w") as u:
            u.write(choice)
        parsed = ai_text(choice)
        output = Handle_command(parsed)
        speak(output)
       

        

