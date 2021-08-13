from controller import Robot, DistanceSensor, Motor

# time in [ms] of a simulation step
TIME_STEP = 64
MAX_SPEED = 6.4

# create the Robot instance.
robot = Robot()
detectRange= 80.0
# initialize devices
ps = []
psNames = [
    'so0', 'so1', 'so2', 'so3',
    'so4', 'so5', 'so6', 'so7'
]

attacking = False
attackLength = 0
aim = "left"
rotateOrMove = 1

for i in range(8):
    ps.append(robot.getDevice(psNames[i]))
    ps[i].enable(TIME_STEP)

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

def facing_enemy(psValues):
    if psValues[3] > detectRange or psValues[4] > detectRange:
        return "facing"
    if psValues[0] > detectRange or psValues[1] > detectRange or psValues[2] > detectRange:
        return "left"
    if psValues[5] > detectRange or psValues[6] > detectRange or psValues[7] > detectRange:
        return "right"
    return "nothing"


while robot.step(TIME_STEP) != -1:
    # read sensors outputs
    psValues = []
    for i in range(8):
        psValues.append(ps[i].getValue())

    facingEnemy = facing_enemy(psValues)
    
    if attacking:
        
        if 60 < attackLength and attackLength < 70:
            if aim == "left":
                leftFrontMotor.setVelocity(-MAX_SPEED)
                leftBackMotor.setVelocity(-MAX_SPEED)
                rightFrontMotor.setVelocity(MAX_SPEED)
                rightBackMotor.setVelocity(MAX_SPEED)
            if aim == "right":
                leftFrontMotor.setVelocity(MAX_SPEED)
                leftBackMotor.setVelocity(MAX_SPEED)
                rightFrontMotor.setVelocity(-MAX_SPEED)
                rightBackMotor.setVelocity(-MAX_SPEED)
        if 20 < attackLength and attackLength < 60:
            leftFrontMotor.setVelocity(MAX_SPEED)
            leftBackMotor.setVelocity(MAX_SPEED)
            rightFrontMotor.setVelocity(MAX_SPEED)
            rightBackMotor.setVelocity(MAX_SPEED)
        if attackLength < 20:
            leftFrontMotor.setVelocity(-MAX_SPEED)
            leftBackMotor.setVelocity(-MAX_SPEED)
            rightFrontMotor.setVelocity(-MAX_SPEED)
            rightBackMotor.setVelocity(-MAX_SPEED)
        attackLength = attackLength - 1
        if attackLength == 0:
            attacking = False

    elif facingEnemy != "nothing":
        aim = facingEnemy
        if aim == "facing":
            attacking = True
            attackLength = 60
        elif aim == "left":
            attacking = True
            attackLength = 70
        elif aim == "right":
            attacking = True
            attackLength = 70

    else:
        if rotateOrMove < 20:
            leftFrontMotor.setVelocity(-MAX_SPEED*0.5)
            leftBackMotor.setVelocity(-MAX_SPEED*0.5)
            rightFrontMotor.setVelocity(MAX_SPEED)
            rightBackMotor.setVelocity(MAX_SPEED)
        elif rotateOrMove < 30:
            leftFrontMotor.setVelocity(MAX_SPEED)
            leftBackMotor.setVelocity(MAX_SPEED)
            rightFrontMotor.setVelocity(MAX_SPEED)
            rightBackMotor.setVelocity(MAX_SPEED)
        elif rotateOrMove < 60:
            leftFrontMotor.setVelocity(MAX_SPEED)
            leftBackMotor.setVelocity(MAX_SPEED)
            rightFrontMotor.setVelocity(-MAX_SPEED*0.5)
            rightBackMotor.setVelocity(-MAX_SPEED*0.5)
        elif rotateOrMove < 65:
            leftFrontMotor.setVelocity(MAX_SPEED)
            leftBackMotor.setVelocity(MAX_SPEED)
            rightFrontMotor.setVelocity(MAX_SPEED)
            rightBackMotor.setVelocity(MAX_SPEED)
        rotateOrMove = rotateOrMove+1
        if rotateOrMove == 65:
            rotateOrMove = 0

