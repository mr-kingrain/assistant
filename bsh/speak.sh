#!/bin/bash

# Check if a pitch argument was given
if [ -z "$1" ]; then
    PITCH=50  # default pitch
else
    PITCH=$1
fi

# Run espeak-ng with the given pitch
espeak-ng -p "$PITCH" -f voice.txt