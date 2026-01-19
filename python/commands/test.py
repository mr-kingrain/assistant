import re

# Known commands (exact matches)
known_commands = [
    "run this app",
    "run this",
    "execute this app",
    "execute the app",
    "start this app",
    "launch this app",
    "open this app",
    "do it",
    "run now",
    "open the app",
    "start the application",
    "run this fucking app or else"
]

# Function to extract app name
def extract_app_name(command):
    cmd_lower = command.strip().lower()
    
    # Ignore exact known commands
    if cmd_lower in known_commands:
        return None
    
    # Remove polite prefixes like 'please' or filler words
    cmd_clean = re.sub(r'^(please|can you|could you|hey)\s+', '', cmd_lower)
    
    # Regex patterns to extract app name (grab last word(s) before 'app')
    patterns = [
        r'run (?:the )?(.+?) app$',       # run spotify app
        r'start (?:the )?(.+)',           # start youtube
        r'launch (?:the )?(.+)',          # launch calculator
        r'open (?:the )?(.+)'             # open spotify
    ]
    
    for pat in patterns:
        match = re.search(pat, cmd_clean)
        if match:
            app_name = match.group(1).strip()
            # Only keep last 1-2 words as app name
            app_name = ' '.join(app_name.split()[-2:])
            return app_name
    
    # If no pattern matches, guess last word as app name
    last_words = cmd_clean.split()[-2:]  # last two words
    return ' '.join(last_words) if last_words else "unknown_app"

# Test commands
test_commands = [
    "open the app",
    "start the ufckiohng YouTube",
    "launch calculator",
    "please run Netflix",
    "can you open Spotify now",
    "hey start the TikTok app"
]

for cmd in test_commands:
    app = extract_app_name(cmd)
    if app:
        print(f"Command: '{cmd}' -> App: '{app}'")
    else:
        print(f"Command: '{cmd}' -> ignored (already known)")