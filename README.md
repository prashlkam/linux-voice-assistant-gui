Liva (linux voice assistant GUI)
================================
 
linux-voice-assistant-gui - a utility that could mimic Cortana on the linux desktop...

Features:-
-----------

Liva provides a basic set of Voice Assistant capabilities including...

* Ability to Record Speech into an Audio file

* Ability to define the Duration of Recording - by editing a config file

* Ability to Convert the Recorded Speech into Text - using the Google Speech to Text API

* Ability to set the Language for the Speech to Text as well as the Text to Speech Engines - by editing the config file

* Once the Speech gets converted to text - it can be copied to the Clipboard (by clicking the Copy button). This text can be pasted into any Application that accepts text inputs (and the entire process can be repeated as many times as required)

* Ability to Recognize a set of Words / Phrases and perform certain Actions Associated with those words / phrases

 [brief list of Phrases and Associated Actions...]

  -> date =  reads out the current system date

  -> time =  reads out the current system time

  -> joke =  tells a joke

  -> news =  gives news headlines (as per config)

  -> weather =  gives Weather (as per config)

  -> play <song> =  plays 'song' on youtube

  -> info page <prog> =  opens info page for 'prog'

  -> man page <prog> =  opens man page for 'prog'

  -> Open in terminal <prog> =  opens  'prog' in terminal

  -> Open <prog> =  opens 'prog' (without terminal)

     {Instead of 'Open' - you may say 'launch', 'open', 'run' or 'start'}

  -> Search Information <phrase> = Search 'phrase' in Google

     {Instead of 'Search' - you may say 'find' or 'search'}

     {Instead of 'information' - you may say 'info' or 'information'}
  -> Ask Questions like the ones shown below - and get answers for the same...
     (A) What is <term>
     (B) Where is <place>
     (C) Who is <person>
     (D) How to <action>

     Note:- Questions such as Which and Why have not been included - as these questions can sometimes be subjective.

     Answers to the available set of questions is fetched by doing a search on Google or a lookup in Wikipedia.


INSTRUCTIONS FOR SETUP...
--------------------------

 * Packages that must be Installed on the system:
  > python3 (if not already installed)
  > python3-pip
  > python3-pyaudio
  > python3-portaudio
  > espeak

 * pip Packages that must be Installed on the system:
  > pyaudio
  > pywhatkit (requires internet connection
  > pyttsx3
  > speechrecognition
  > pyjokes
  > python-weather
  > gnewsclient
  > pyqt5
  > datetime
  > requests
  > asyncio
  > python-Levenshtein

 * pip Packages that must be Excluded on the system:
  > mouseinfo (if already installed - please Uninstall)


Setup Process...
-----------------


