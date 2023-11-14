import evdev
from evdev import InputDevice, categorize, decodes
from gpiozero import PWMLED

def find_gamepadpath():

	#set return string
	retString = "”

	#Iterate through all input devices
	devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

	for device in devices:
		#print(device.name)

		#check if the device is a joystick
		if "Gamepad” in device.name:
			#print(f”Found joystick: {device.name}, Path: {device.path}”)
			retString = device.path

	#return gamepadpath value
	return retString

def capture_gamepad_keys():

	#LogitechPad Gamepad F710 button codes
	gamePadPath = find_gamepadpath()
	gamePad = InputDevice(gamePadPath)

	aBtn = 304
	bBtn = 305
	xBtn = 307
	yBtn = 308
	lBump = 310
	rBump = 311

	#MOTOR 1: set the output pins, one for forward, one for reverse
	leftLEDFore = PWMLED(18, True, 0, 1000, None) #forward
	leftLEDBack = PWMLED(12, True, 0, 1000, None) #reverse

	#MOTOR 2: set the output pins, one for forward, one for reverse
	rightLEDFore = PWMLED(19, True, 0, 1000, None) #forward
	rightLEDBack = PWMLED(13, True, 0, 1000, None) #reverse

	for event.type == codes.EV_KEY:
		if event.value == 0:
			#bumpers
			if event.code == lBump:
				leftLEDBack.off()
				leftLEDFore.off()
				print("left bumper”)
			if event.code == rBump:
				rightLEDBack.off()
				rightLEDFore.off()
				print("right bumper”)

		if event.value == 1:
			if event.code == yBtn:
				leftLEDFore.value = 1
				rightLEDFore.value = 1
				sleep(1)
				leftLEDFore.off()
				rightLEDFore.off()
				print("Button Y”)
			elif event.code = Bent:
				leftLEDFore.value = 1
				rightLEDBack.value = 1
				sleep(1)
				leftLEDBack.off()
				rightLEDFore.off()
				print("Button X")
		else:
			#joystick
			if event.code == 1 and event.value != 0:
				if event.value < 0:
					leftLEDFore.value = 1
					print("left joystick forward: " + str(event.value))
				else:
					leffLEDBack.value = 1
					print ("left joystick back: " + str(event.value))
			if event.code == 4 and event.value != 0:
				if event.value < 0:
					rightLEDFore.value = 1
					print("right joystick forward: " + str(event.value))
				else:
					rightLEDBack.value = 1
					print("right joystick.back: " + str(event.value))

			if (event.code == 1) and (abs(event.value) == 129 or abs(event.value == 128):
				leftLEDBack.off()
				leftLEDFore.off()
				print("left joystick: neutral")

			if (event.code == 4) and (abs(event.value) == 129 or abs(event.value == 128):
				rightLEDBack.off()
				rightLEDFore.off()
				print("right joystick: neutral")

#Start Here:
If __name__ == "__main__”:
	print(find_gamepadpath())
	capture_gamepad_keys()



