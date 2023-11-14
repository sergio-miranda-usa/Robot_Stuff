{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww9780\viewh18400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import evade\
from evade import InputDevice, categorize, decodes\
from gpiozero import PWMLED\
\
def find_gamepadpath():\
\
	#set return string\
	retString = \'93\'94\
\
	#Iterate through all input devices\
	devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]\
\
	for device in devices:\
		#print(device.name)\
\
		#check if the device is a joystick\
		if \'93Gamepad\'94 in device.name:\
			#print(f\'94Found joystick: \{device.name\}, Path: \{device.path\}\'94)\
			retString = device.path\
\
	#return gamepadpath value\
	return retString\
\
def capture_gamepad_keys():\
\
	#LogitechPad Gamepad F710 button codes\
	gamePadPath = find_gamepadpath()\
	gamePad = InputDevice(gamePadPath)\
\
	aBtn = 304\
	bBtn = 305\
	xBtn = 307\
	yBtn = 308\
	lBump = 310\
	rBump = 311\
\
	#MOTOR 1: set the output pins, one for forward, one for reverse\
	leftLEDFore = PWMLED(18, True, 0, 1000, None) #forward\
	leftLEDBack = PWMLED(12, True, 0, 1000, None) #reverse\
\
	#MOTOR 2: set the output pins, one for forward, one for reverse\
	rightLEDFore = PWMLED(19, True, 0, 1000, None) #forward\
	rightLEDBack = PWMLED(13, True, 0, 1000, None) #reverse\
\
	for event.type == codes.EV_KEY:\
		if event.value == 0:\
			#bumpers\
			if event.code == lBump:\
				leftLEDBack.off()\
				leftLEDFore.off()\
				print(\'93left bumper\'94)\
			if event.code == rBump:\
				rightLEDBack.off()\
				rightLEDFore.off()\
				print(\'93right bumper\'94)\
\
		if event.value == 1:\
			if event.code == yBtn:\
				leftLEDFore.value = 1\
				rightLEDFore.value = 1\
				sleep(1)\
				leftLEDFore.off()\
				rightLEDFore.off()\
				print(\'93Button Y\'94)\
			elif event.code = Bent:\
				leftLEDFore.value = 1\
				rightLEDBack.value = 1\
				sleep(1)\
				leftLEDBack.off()\
				rightLEDFore.off()\
				print(\'93Button X\'94)\
		else:\
			#joystick\
			if event.code == 1 and event.value != 0:\
				if event.value < 0:\
					leftLEDFore.value = 1\
					print(\'93left joystick forward: \'93 + str(event.value))\
				else:\
					leffLEDBack.value = 1\
					print (\'93left joystick back: \'93 + str(event.value))\
			if event.code == 4 and event.value != 0:\
				if event.value < 0:\
					rightLEDFore.value = 1\
					print(\'93right joystick forward: \'93 + str(event.value))\
				else:\
					rightLEDBack.value = 1\
					print(\'93right joystick.back: \'93 + str(event.value))\
\
#Start Here:\
If __name__ == \'93__main__\'94:\
	print(find_gamepadpath())\
	capture_gamepad_keys()\
\
\
\
}