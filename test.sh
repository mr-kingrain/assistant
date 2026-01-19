#!/bin/bash

face=("  ^_^  "
      " (o o) "
      "  \_/  ")

# Width reserved for face
face_width=12

# Function to print face alongside lines
function print_line() {
    local left="$1"
    local right="$2"
    printf "%-${face_width}s | %s\n" "$left" "$right"
}

# Function to redraw face and previous output
function draw_terminal() {
    clear
    # Print face
    for line in "${face[@]}"; do
        print_line "$line" ""
    done
    # Print previous output
    for line in "${history[@]}"; do
        print_line "" "$line"
    done
}

# Array to store output history
history=()

while true; do
    draw_terminal
    # Prompt
    read -p " > " cmd

    if [[ "$cmd" == "exit" || "$cmd" == "quit" ]]; then
        break
    fi

    # Run command and capture output
    output=$(eval "$cmd" 2>&1)
    while IFS= read -r line; do
        history+=("$line")
    done <<< "$output"
done