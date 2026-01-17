#!/bin/bash

PING_TARGET="8.8.8.8"
ONLINE=false

echo "Checking internet connection..."
if ping -c 1 -W 2 $PING_TARGET >/dev/null 2>&1; then
    ONLINE=true
    echo "Internet: online"
else
    echo "Internet: offline"
fi

if [ "$ONLINE" = true ]; then
    echo "Updating system..."
    sudo apt update && sudo apt upgrade -y

    echo "Removing unused packages..."
    sudo apt autoremove -y
    sudo apt autoclean -y

    echo "Clearing APT cache..."
    sudo rm -rf /var/cache/apt/archives/*

    echo "Cleaning unused Flatpak stuff..."
    if command -v flatpak >/dev/null 2>&1; then
        flatpak uninstall --unused -y
    else
        echo "Flatpak not installed. Skipping."
    fi
else
    echo "Skipping network-related commands."
fi

echo "Cleaning user cache..."
rm -rf ~/.cache/*

echo "Cleaning old logs (keep 7 days)..."
sudo journalctl --vacuum-time=7d

echo "Cleanup finished."