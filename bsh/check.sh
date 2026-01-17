#!/bin/bash

DOCS="$HOME/Documents"
FOLDER="$DOCS/butlerenv"

if [ -d "$FOLDER" ]; then
    echo "Folder 'butlerenv' already exists in Documents."
else
    echo "Folder 'butlerenv' does NOT exist in Documents."
fi