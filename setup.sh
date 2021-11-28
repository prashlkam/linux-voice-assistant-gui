#!/bin/bash

## Uncomment appropriate line as per your distro - and then run
## ============================================================
# sudo dnf install -y python3-pip python3-pyaudio espeak
# sudo apt-get install -y python3-pip python3-pyaudio espeak
# paru -Sy python3-pip python3-pyaudio espeak

## same commands for all distros
## =================================
pip -q install speechrecognition pyttsx3 pyqt5 pyaudio pywhatkit pyjokes datetime requests gnewsclient asyncio python-weather python-Levenshtein
pip -q --no-input uninstall mouseinfo

clear

mkdir ~/.config/liva
mkdir ~/.config/liva/tmp

cp ./res/liva-config.json ~/.config/liva/liva-config.json

clear



