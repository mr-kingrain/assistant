from python.commands.test import hello
from python.commands.apt import apt 
from python.commands.apt import default_pswd as DP
from python.commands.apt import passwd 
from python.commands.clean import clean
from python.speak import talk 

import threading

def speak(a):
    t = threading.Thread(target=talk, args=(a,))
    t.start()

def handleC(text):

    output = ""


    match text:
        case "hi":
            output = "no"
        case "print":
            output = "ok"
            hello()
        case "sudo pass":
            speak('Enter Default password')
            DP()

        case "apt update":
            apt(1,passwd())
            talk("apt update complete")

        case "clean":
            talk("i shall clean youre pc now master")
            clean(passwd())
            talk("youre pc is now clean master")
            
        case "":
            output = "type something"


    return output
    pass
