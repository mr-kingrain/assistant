import subprocess




def setuping():
    # Path to your bash script
    bash_script = "bsh/setup.sh"
    setuped = False
    try:
        # Run the bash script and capture output
        result = subprocess.run(["bash", bash_script], capture_output=True, text=True, check=True)
        
        output = result.stdout.strip()
        print(output)  # Print the message from Bash

        # Check if folder already exists
        if "already exists" in output:
            setuped = True
        else:
            setuped = False
    except subprocess.CalledProcessError as e:
        print("Error running the script:")
        print(e.stderr)
    
    return setuped




def check():
    # Path to your bash script
    bash_script = "bsh/check.sh"
    setuped = False
    try:
        # Run the bash script and capture output
        result = subprocess.run(["bash", bash_script], capture_output=True, text=True, check=True)
        
        output = result.stdout.strip()
        print(output)  # Print the message from Bash

        # Check if folder already exists
        if "already exists" in output:
            setuped = True
        else:
            setuped = False
    except subprocess.CalledProcessError as e:
        print("Error running the script:")
        print(e.stderr)
    
    return setuped
