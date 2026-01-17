import subprocess
import threading

def talk(a):
    with open("test.txt", "w") as f:
        f.write(a)
    subprocess.run(["bash", "bsh/test.sh"], check=True)


# t.join()  # uncomment if you need to wait