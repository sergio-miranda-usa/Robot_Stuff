import evdev
from evdev import InputDevice, categorize
import motoron

def find_gamepadpath():
    
    #set return string
    retString = ""
    
    #iterate through all input devices
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    
    for device in devices:
        #print all devices attached to the box
        #print (device.name)
        
        #check if the device is a joystick
        if "Gamepad" in device.name:
            print(device.name)
            retString = device.path
    
    return retString

def capture_gamepad_keys(gamePadPath):
    
    deadZone = 670
    
    #print the controller path
    print(gamePadPath)
    
    #get device from path
    gamePad = InputDevice(gamePadPath)
    
    #interrogate the pad for events
    for event in gamePad.read_loop():
        
        print(categorize(event))
        print(str(event.code) + " : " + str(event.value))
                
        #304 A
        #308 Y
        #305 B
        #307 X
        #310 LB
        #311 RB
        #2  LT
        #5  RT
        #16 DPad R L
        #17 DPad Up Down
        
        #according to the button pressed, activate motor
        if event.code == 308: #BTN_Y
            if event.value == 1: #down
                motor_forward()
            elif event.value == 0: #up
                motor_stop()
        #moves backwards 
        if event.code == 304: #BTN_A
            if event.value == 1:#down
                motor_backward()
            elif event.value == 0: #up
                motor_stop()
       #move right          
        if event.code == 305: #BTN_B
            if event.value == 1:#down
                motor_right()
            elif event.value == 0: #up
                motor_stop()
      #moves left           
        if event.code == 307: #BTN_X
            if event.value == 1:#down
                motor_left()
            elif event.value == 0: #up
                motor_stop()
        
         
        if event.code == 1: # ABS_Y
            #print("joystick left")
            if event.value < -deadZone:
                print("joystick left up")
                motor_forward_left(event.code)
            if event.value > deadZone:
                print("joystick left down")
                motor_backward_left(event.code)
            if event.value <= deadZone and event.value >= -deadZone:
                print("joystick left deadzone")
                motor_stop_left()
                
        if event.code == 3: # ABS_X
            #print("joystick right x")
            if event.value <= deadZone and event.value >= -deadZone:
                print("joystick right deadzone")
                motor_stop_right()
                
        if event.code == 4: # ABS_Y
            #print("joystick right")
            if event.value < -deadZone:
                print("joystick right up")
                motor_forward_right(event.code)
            if event.value > deadZone:
                print("joystick right down")
                motor_backward_right(event.code)
            if event.value <= deadZone and event.value >= -deadZone:
                print("joystick right deadzone")
                motor_stop_right()
                    
def motor_forward():
    #move motors forward
    mc.set_speed(1,400)
    mc.set_speed(2,-360) #negative because it is facing opposite

def motor_forward_left(valJoystick):
    #move left motor forward
    print(str(valJoystick))
    mc.set_speed(1,800)
    
def motor_backward_left(valJoystick):
    #move left motor forward
    print(str(valJoystick))
    mc.set_speed(1,-800)
    
def motor_forward_right(valJoystick):
    #move right motor forward
    print(str(valJoystick))
    mc.set_speed(2,-800)
    
def motor_backward_right(valJoystick):
    #move right motor backward
    print(valJoystick)
    mc.set_speed(2,800)
    
def motor_backward():
    #move motors backward
    mc.set_speed(1,-400)
    mc.set_speed(2,400)
    
def motor_right():
    #move motors right
    mc.set_speed(1,400)
    mc.set_speed(2,400)
    
def motor_left():
    #move motors left
    mc.set_speed(1,-400)
    mc.set_speed(2,-400)

def motor_stop():
    #stop all motors to freewheel
    mc.coast_now()
    
def motor_stop_right():
    #stop all motors to freewheel
    mc.set_speed(2,0)

def motor_stop_left():
    #stop all motors to freewheel
    mc.set_speed(1,0)

#Start Here:
mc = motoron.MotoronI2C()
mc.reinitialize()
mc.disable_crc()
mc.clear_reset_flag()
mc.disable_command_timeout()

#Get gamepad
gamePadPath = find_gamepadpath()
capture_gamepad_keys(gamePadPath)


