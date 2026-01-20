from python.commands.apt import apt 
from python.commands.apt import default_pswd as DP
from python.commands.apt import passwd 
from python.commands.pc import clean,healthchk,internet_test
from python.commands.run import run
from python.commands.music import play_music,pause_music
from python.speak import talk 
from python.speak import tspeak as speak

import threading



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
        case "pause_music":
            pause_music()
        case "healthchk":
            healthchk()
        case "internet_test":
            internet_test()



        case "clean":
            talk("i shall clean youre pc now master")
            clean(passwd())
            talk("youre pc is now clean master")
            
        case "" :
            output = "type something"
        case "unknown":  
            output = "enter a proper command"


    return output
    pass
