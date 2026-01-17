#!/bin/bash

# Default Documents folder
DOCS="$HOME/Documents"

# New folder path
NEW_FOLDER="$DOCS/butlerenv"

# Check if folder already exists
if [ -d "$NEW_FOLDER" ]; then
    echo "Folder 'butlerenv' already exists in Documents."
else
    mkdir "$NEW_FOLDER"
    echo "Folder 'butlerenv' created in Documents."
fi


# Default Documents folder
SCRIPTS="$HOME/Documents/butlerenv"

# New folder path
NEWW_FOLDER="$SCRIPTS/scripts"

# Check if folder already exists
if [ -d "$NEWW_FOLDER" ]; then
    echo "Folder 'scripts' already exists in Documents."
else
    mkdir "$NEWW_FOLDER"
    echo "Folder 'scripts' created in Documents."
fi