from controller import Robot
from controller import LED

robot = Robot()

time = int(robot.getBasicTimeStep())

ds = []
ds_names = ["ds_right", "ds_left", "ds_mid_right", "ds_mid_left","ds_right_wall", "ds_left_wall", "ds_front_wall"]
ds_val = [0]*len(ds_names)

for name in ds_names:

    ds.append(robot.getDevice(name))
    ds[-1].enable(time)
    
wheels =[]
wheel_names = ["front_right_motor", "front_left_motor", "rear_right_motor", "rear_left_motor"]    

for name in wheel_names:

    wheels.append(robot.getDevice(name))
    wheels[-1].setPosition(float('inf'))
    wheels[-1].setVelocity(0.0)

led =[]
led_names = ["led_right", "led_mid", "led_left"]    

for name in led_names:

    led.append(robot.getDevice(name))

last_error = intg = diff = prop = 0
kp = 0.0009
ki = 0
kd = 0.001    

def pid(error):

    global last_error, intg, diff, prop, kp, ki, kd
    prop = error
    intg = error + intg
    diff = error - last_error
    balance = (kp*prop) + (ki*intg) + (kd*diff)
    last_error = error
    return balance

def setSpeed(base_speed, balance):

    wheels[0].setVelocity(base_speed + balance)
    wheels[1].setVelocity(base_speed - balance)
    wheels[2].setVelocity(base_speed + balance)
    wheels[3].setVelocity(base_speed - balance)

stop = 0

while robot.step(time) != -1:

    for i in range(len(ds)):
    
        ds_val[i] = ds[i].getValue()
        print(f"{ds_names[i]} : {ds_val[i]}\n" + "*"*40 )
   
    if ds_val[2] < 350 and ds_val[3] < 350:
            error = 0
            rectify = pid(error)
            print(rectify)
            setSpeed(1,-1*rectify)
            led[1].set(0)
            print("Case 0")
            
            if ds_val[4] < 950:
                led[0].set(1)
                
            elif ds_val[4] > 950:
                led[0].set(0) 
            
            if ds_val[5] < 950:
                led[2].set(1)
                
            elif ds_val[5] > 950:
                led[2].set(0)         
              
            if ds_val[0] < 450 and ds_val[1] < 450:
               led[0].set(1)
               led[1].set(1)
               led[2].set(1)
               
    elif ds_val[2] < 950 and ds_val[3] < 950 and ds_val[0] < 950 and ds_val[1] < 950:
            print("Case 00")
            led[1].set(0)
            
            if ds_val[4] < 950:
                led[0].set(1)
                
            elif ds_val[4] > 950:
                led[0].set(0) 
            
            if ds_val[5] < 950:
                led[2].set(1)
                
            elif ds_val[5] > 950:
                led[2].set(0)         
            
            if ds_val[6] < 950:
                error = ds_val[6] - 900
                rectify = pid(error)
                print(rectify)
                setSpeed(0.2,rectify)
                print("Case 01")
                
            if ds_val[4] < 950 and ds_val[5] > 950:
                error = 0
                rectify = pid(error)
                print(rectify)
                setSpeed(1,-1*rectify)
                print("Case 02") 
                stop = 1
                
                if ds_val[4] < 350:
                    error = ds_val[4] - 150
                    rectify = pid(error)
                    print(rectify)
                    setSpeed(0.2,rectify)
                    print("Case 02A")
           
            if ds_val[5] < 950 and ds_val[4] > 950:
                error = 0
                rectify = pid(error)
                print(rectify)
                setSpeed(1,-1*rectify)
                print("Case 03")
                
                if ds_val[5] < 200:
                    error = ds_val[5] - 50
                    rectify = pid(error)
                    print(rectify)
                    setSpeed(0.1,-1*rectify)
                    print("Case 03A")
            
            if ds_val[4] < 950 and ds_val[6] != 1000:
                    error = ds_val[4] - 170
                    rectify = pid(error)
                    print(rectify)
                    setSpeed(0.4,rectify)
                    print("Case 04") 
                        
            elif ds_val[5] < 950 and ds_val[6] != 1000:
                    error = ds_val[4] - 800
                    rectify = pid(error)
                    print(rectify)
                    setSpeed(0.4, -1*rectify) 
                    print("Case 05")
              
            elif ds_val[5] > 450 and ds_val[6] == 1000 and ds_val[4] > 950:
                    error = ds_val[5] - 400
                    rectify = pid(error)
                    print(rectify)
                    setSpeed(0.4,rectify)
                    print("Case 06")
                           
    elif ds_val[2] > 500 and ds_val[3] < 500:
            error = ds_val[3] - 30
            rectify = pid(error)
            print(rectify)
            setSpeed(0.4,rectify)
            print("Case 1")
                
    elif ds_val[2] < 500 and ds_val[3] > 500:
            error = ds_val[2] - 30
            rectify = pid(error)
            print(rectify)
            setSpeed(0.4,-1*rectify)
            print("Case 2")         
           
    elif ds_val[0] > 950 and ds_val[1] > 950 and ds_val[2] > 950 and ds_val[3] > 950:
            error = 0
            rectify = pid(error)
            print(rectify)
            setSpeed(1,-1*rectify)
            led[1].set(1)
            print("Case 3")
            if stop == 1:
                setSpeed(0,0)
                
    elif ds_val[0] < 950 and ds_val[1] > 950 and ds_val[2] > 950 and ds_val[3] > 950:
            error = ds_val[0] - 380
            rectify = pid(error)
            print(rectify)
            setSpeed(0.4,rectify)
            print("Case 4") 
                           
    elif ds_val[0] > 950 and ds_val[1] < 950 and ds_val[2] > 950 and ds_val[3] > 950:
            error = ds_val[1] - 380
            rectify = pid(error)
            print(rectify)
            setSpeed(0.4,-1*rectify)
            print("Case 5")  
           
    pass
