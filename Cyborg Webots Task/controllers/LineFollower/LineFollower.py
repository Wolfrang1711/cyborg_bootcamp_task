"""LineFollower controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
    
motorFR = robot.getDevice('front_right_motor')
motorFL = robot.getDevice('front_left_motor')
motorRR = robot.getDevice('rear_right_motor')
motorRL = robot.getDevice('rear_left_motor')

motorFR.setPosition(float('inf'))
motorFL.setPosition(float('inf'))
motorRR.setPosition(float('inf'))
motorRL.setPosition(float('inf'))
    
motorFR.setVelocity(0.0)
motorFL.setVelocity(0.0)
motorRR.setVelocity(0.0)
motorRL.setVelocity(0.0)
    
ds_right = robot.getDevice('ds_right')
ds_left = robot.getDevice('ds_left')
ds_detect = robot.getDevice('ds_detect')
    
ds_right.enable(timestep)
ds_left.enable(timestep) 
ds_detect.enable(timestep)  

# Main loop:
# - perform simulation steps until Webots is stopping the controller        

start = 0

while robot.step(timestep) != -1:

    val_right = ds_right.getValue()
    val_left = ds_left.getValue()
    val_detect = ds_detect.getValue()
    #print(val_right, val_left)
    #print(val_detect)
    
    if val_detect < 1000:
        start = 1     
        
       
    if val_right == 1000 and val_left == 1000 and start == 1:
        #move forward
        #print("moving forward")
        motorFR.setVelocity(8.0)
        motorFL.setVelocity(8.0)
        motorRR.setVelocity(8.0)
        motorRL.setVelocity(8.0)    
         
    if val_right < 1000 and val_left == 1000 and start == 1:
        #move left
        #print("moving left") 
        motorFR.setVelocity(8.0)
        motorFL.setVelocity(-8.0)
        motorRR.setVelocity(8.0)
        motorRL.setVelocity(-8.0)  
        
    if val_right == 1000 and val_left < 1000 and start == 1:
        #move right
        #print("moving right")  
        motorFR.setVelocity(-8.0)
        motorFL.setVelocity(8.0)
        motorRR.setVelocity(-8.0)
        motorRL.setVelocity(8.0)  

    if val_right < 1000 and val_left < 1000 and start == 1:   
        #stop
        #print("at halt")    
        motorFR.setVelocity(0.0)
        motorFL.setVelocity(0.0) 
        motorRR.setVelocity(0.0)
        motorRL.setVelocity(0.0)
       
    pass

# Enter here exit cleanup code.
