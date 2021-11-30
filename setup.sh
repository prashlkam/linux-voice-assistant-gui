#!/bin/bash

## Uncomment appropriate line as per your distro - and then run
## ============================================================


# For Red Hat based distros...
if ! dnf -V | grep -q 'Could not find Command'; then
    sudo dnf install -y python3-pip python3-pyaudio espeak
fi

# For Debian based distros...
if ! apt-get -V | grep -q 'Could not find Command'; then
    sudo apt-get install -y python3-pip python3-pyaudio espeak
fi

# For Arch based distros...
if ! pacman -V | grep -q 'Could not find Command'; then
    sudo pacman -Syy python3-pip python3-pyaudio espeak
fi

## same commands for all distros
## =================================
pip -q install speechrecognition pyttsx3 pyqt5 pyaudio pywhatkit pyjokes datetime requests gnewsclient asyncio python-weather python-Levenshtein
pip -q uninstall mouseinfo

clear

mkdir ~/.config/liva
mkdir ~/.config/liva/tmp

cp ./res/liva-config.json ~/.config/liva/liva-config.json

clear



