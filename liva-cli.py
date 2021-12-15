#!/usr/bin/env python3

import sys
import os
import livavoice as liva

def main():
	print('Welcome to Liva-CLI - a CLI Voice Assistant on Linux...')
	print('========================================================')
	print('')
	print('Liva-CLI runs in a Loop mode. When the Loop Starts, You can...')
	print('Press \'I\' or \'i\' for instructions...')
	print('Press \'S\' or \'s\' for settings (requires vim)...')
	print('Press \'Q\' or \'q\' to quit...')
	print('Press any other key to continue looping...')
	opt = input(' Now Press <enter> to begin: ')
		 
	while not 'q' in opt[0].lower():
		liva_obj = liva.LivaVoice()
		os.system('clear')
		print('Start speaking when you see \'Recording...\'')
		print('Stop when you see \'Finished recording...\'')
		input('Press <enter> when you\'re ready to start Recording...')
		cmd = liva_obj.take_command()
		print('\nWhat do you want to do with the Speech converted to Text? : ')
		print('Press \'r\' to Run | \'a\' to Append to File | \'i\' for Instructions\n	  \'s\' for Settings | \'t\' to type Command\n	  \'q\' to Quit | Any other key to continue...')
		opt = input('Enter your choice: ')
		if 'r' in opt[0].lower():
			liva_obj.run_liva(cmd)
		elif 't' in opt[0].lower():
			cmd = input('Type in the Command for Liva: ')
			liva_obj.run_liva(cmd)
		elif 'a' in opt[0].lower():
			append_file(cmd)
		elif 'i' in opt[0].lower():
			info_func()
		elif 's' in opt[0].lower():
			settings_func()
		elif 'q' in opt[0].lower():
			exit()
		else:
			input('Press <enter> to clear the Screen and proceed...')
			os.system('clear')

def append_file(cmd):
	print('Appending text to file \'~/Documents/liva-conv01.txt\'...')
	with open(os.path.expanduser('~/Documents/liva-conv01.txt'),'a') as outfile:
		outfile.write(cmd)

def info_func():
	print('Instructions to use Liva-cli more effectively...')
	print('1/ Ensure that your Mic is plugged in, configured properly and ready to use. At present, Liva doesn\'t provide any sort of interface to help you setup / configure / troubleshoot your sound devices setup.')
	print('2/ Test your sound setup - before you start using Liva. Use your DE\'s Sound Settings to configure your Sound Devices. You can find these settings in your respective DE\'s Control Panel / System Settings. Then Test everything using an App such as Zoom. If everything is working - you\'re good to go. ')
	print('3/ Now Launch Liva-cli by running the appropriate command. You might see some errors / warnings related to ALSA / Jack - these relate to the way these softwares are configured on your system. If your sound hardware (Mic and Speakers) are working fine - then you don\'t need to worry much about these errors / warnings. ')
	print('4/ Once the program runs - it provides a set of on-screen instructions. Following the on-screen alerts and prompts AND providing the right input at every stage - should help you navigate through the program effectively. ')
	print('5/ There is a config file located at \'~/.config/liva/\' (where \'~\' denotes the active user\'s home directory). You may edit this file to tweak some of the settings. CAUTION: Do not change the settings in this file - unless you know exactly what you\'re doing... ')
	print('6/ For info on setup / requirements / dependecies / general usage - please refer to the Readme file on github and the man page for Liva...')
	print('7/ You may report any issues / problems / bugs etc. on github. Or you may fork the project and improve it further. ')
	print('Last but not least - I created Liva in order to address a very specific gap in Linux. I hope some of you will find my work useful in some way - and the idea behind this app survives and becomes better over time... Thank you for using Liva... :) ')

def settings_func():
	print('Opening Settings file...')
	term = 'xterm '
	cmd = ' vim ~/.config/liva/liva-config.json'
	os.popen(term + ' -hold -e ' + cmd)

main()
