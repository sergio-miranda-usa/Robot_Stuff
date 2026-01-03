from fastapi import FastAPI
import uvicorn
import motoron
import time

app = FastAPI(title="Tanker REST API")


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

app = FastAPI(title="Tanker REST API")

#Define APIs
@app.get("/forward/{a}")
def add(a: int):
    motor_forward()
    time.sleep(a)
    motor_stop()
    return {f"forward for {a}s"}

@app.get("/back/{a}")
def add(a: int):
    motor_backward()
    time.sleep(a)
    motor_stop()
    return {f"back for {a}s"}

@app.get("/spinright/{a}")
def add(a: int):
    motor_right()
    time.sleep(a)
    motor_stop()
    return {f"spin right for {a}s"}

@app.get("/spinleft/{a}")
def add(a: int):
    motor_left()
    time.sleep(a)
    motor_stop()
    return {f"spin left for {a}s"}

if __name__ == "__main__":
    
    uvicorn.run(
        app,
        host="0.0.0.0", #Bind to all network interfaces
        port="8000",
        reload=False
        )
        