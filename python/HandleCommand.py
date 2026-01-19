from python.commands.apt import apt 
from python.commands.apt import default_pswd as DP
from python.commands.apt import passwd 
from python.commands.clean import clean
from python.speak import talk 
from python.commands.run import run
from python.commands.play_music import play_music

import threading

def speak(a):
    t = threading.Thread(target=talk, args=(a,))
    t.start()

def handleC(a):

    output = ""

    text = a.lower()


    match text:
        case "help":
            output = " lol no"
        case "hi":
            output = "no"
        case "sudo pass":
            speak('Enter Default password')
            DP()

        case "apt update":
            apt(1,passwd())
            talk("apt update complete")
        case "run_app":
            run()
        case "play_music":
            play_music()


        case "clean":
            talk("i shall clean youre pc now master")
            clean(passwd())
            talk("youre pc is now clean master")
            
        case "" :
            output = "type something"
        case "unknown":  
            output = "speak clearly please"


    return output
    pass
