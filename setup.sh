#!/bin/bash

## Linux Voice Assistant - Initial Setup Script
## ============================================================


## Uncomment appropriate line as per your distro - and then run
## ============================================================


# For Red Hat based distros...
if ! [dnf | grep -q 'command not found']; then
    sudo dnf install -y python3-pip python3-pyaudio espeak
fi	

# For Debian based distros...
if ! [apt-get | grep -q 'command not found']; then
    sudo apt-get install -y python3-pip python3-pyaudio espeak
fi

# For Arch based distros...
if ! [pacman | grep -q 'command not found']; then
    sudo pacman -Syy python3-pip python3-pyaudio espeak
fi
## for all other distros
## ========================

# find your distro's package manager using a command like:
# apropos 'package manager' | more

# then read the man page for your package manager using the command:
# man <your_distro_package_manager>

# finally install the above packages using your distro's package manager
# examples:
# sudo zypper install -y python3-pip python3-pyaudio espeak
# sudo emerge -al python3-pip python3-pyaudio espeak
# sudo slackpkg install python3-pip python3-pyaudio espeak


## same commands for all distros
## =================================
pip -q install speechrecognition pyttsx3 pyqt5 pyaudio pywhatkit pyjokes datetime requests gnewsclient asyncio python-weather python-Levenshtein
pip -q uninstall mouseinfo

clear

sudo mkdir /usr/share/linux-voice-assistant
mkdir ~/.config/liva
mkdir ~/.config/liva/tmp

sudo cp -R ./*  /usr/share/linux-voice-assistant
cp ./res/liva-config.json ~/.config/liva


sudo chmod +x  /usr/share/linux-voice-assistant/liva-gui.py
sudo chmod +x  /usr/share/linux-voice-assistant/liva-cli.py

sudo cp ./res/Liva-GUI.desktop  /usr/share/applications

clear
