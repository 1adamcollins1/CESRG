from controller import Robot, DistanceSensor, Motor

# time in [ms] of a simulation step
TIME_STEP = 64

MAX_SPEED = 6.4

# create the Robot instance.
robot = Robot()


leftFrontMotor = robot.getDevice('front left wheel')
rightFrontMotor = robot.getDevice('front right wheel')
leftBackMotor = robot.getDevice('back left wheel')
rightBackMotor = robot.getDevice('back right wheel')
leftFrontMotor.setPosition(float('inf'))
rightFrontMotor.setPosition(float('inf'))
leftBackMotor.setPosition(float('inf'))
rightBackMotor.setPosition(float('inf'))
leftFrontMotor.setVelocity(0)
rightFrontMotor.setVelocity(0)
leftBackMotor.setVelocity(0)
rightBackMotor.setVelocity(0)

# feedback loop: step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:
    # read sensors outputs

    # initialize motor speeds at 50% of MAX_SPEED.
    leftSpeed  = 0.9 * MAX_SPEED
    rightSpeed = 0.9 * MAX_SPEED
 
    # write actuators inputs
    leftFrontMotor.setVelocity(MAX_SPEED)
    rightFrontMotor.setVelocity(MAX_SPEED)
    leftBackMotor.setVelocity(MAX_SPEED)
    rightBackMotor.setVelocity(MAX_SPEED)