import motoron
import time

def motor_forward():
    #move motors forward
    mc.set_speed(1,400)
    mc.set_speed(2,-360) #negative because it is facing opposite

def motor_forward_left():
    #move left motor forward
    mc.set_speed(1,800)
    
def motor_backward_left():
    #move left motor forward
    mc.set_speed(1,-800)
    
def motor_forward_right():
    #move right motor forward
    mc.set_speed(2,-800)
    
def motor_backward_right():
    #move right motor backward
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

#run test
motor_forward()
time.sleep(30)
motor_stop()
