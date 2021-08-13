from controller import Supervisor, Keyboard, Robot
import sys, os

TIME_STEP = 64

supervisor = Supervisor()
keyboard = Keyboard()

keyboard.enable(10)

robot_node1 = supervisor.getFromDef("ROBOT_1")
robot_node2 = supervisor.getFromDef("ROBOT_2")
death_zone1 = supervisor.getFromDef("DEATHZONE_1")
death_zone2 = supervisor.getFromDef("DEATHZONE_2")

trans_field1 = robot_node1.getField("translation")
trans_field2 = robot_node2.getField("translation")
deathzone_xyz1 = death_zone1.getField("translation").getSFVec3f()
deathzone_xyz2 = death_zone2.getField("translation").getSFVec3f()
robot1cont = robot_node1.getField("controller")
robot2cont = robot_node2.getField("controller")
cont1str = robot1cont.getSFString()
cont2str = robot2cont.getSFString()

simulationDone = 0

def robot_in_zone (robot_xyz, zone_xyz, zone_size):
    catch_zone = zone_size/2
    if ((zone_xyz[2]- catch_zone < robot_xyz[2])and(zone_xyz[2]+ catch_zone > robot_xyz[2])):
        if ((zone_xyz[0]- catch_zone < robot_xyz[0])and(zone_xyz[0]+ catch_zone > robot_xyz[0])):
            return bool(1)
    return bool(0)

def robot_below_zone (robot_xyz, zone_xyz):
    if (zone_xyz[1] > robot_xyz[1]):
        return bool(1)
    return bool(0)

def cage_death (robot_xyz, zone_size):
    catch_zone = zone_size/2
    if ((deathzone_xyz1[2]- catch_zone < robot_xyz[2])and(deathzone_xyz1[2]+ catch_zone > robot_xyz[2])):
        if ((deathzone_xyz1[0]- catch_zone < robot_xyz[0])and(deathzone_xyz1[0]+ catch_zone > robot_xyz[0])):
            return bool(1)
    if ((deathzone_xyz2[2]- catch_zone < robot_xyz[2])and(deathzone_xyz2[2]+ catch_zone > robot_xyz[2])):
        if ((deathzone_xyz2[0]- catch_zone < robot_xyz[0])and(deathzone_xyz2[0]+ catch_zone > robot_xyz[0])):
            return bool(1)
    if ((deathzone_xyz3[2]- catch_zone < robot_xyz[2])and(deathzone_xyz3[2]+ catch_zone > robot_xyz[2])):
        if ((deathzone_xyz3[0]- catch_zone < robot_xyz[0])and(deathzone_xyz3[0]+ catch_zone > robot_xyz[0])):
            return bool(1)
    if ((deathzone_xyz4[2]- catch_zone < robot_xyz[2])and(deathzone_xyz4[2]+ catch_zone > robot_xyz[2])):
        if ((deathzone_xyz4[0]- catch_zone < robot_xyz[0])and(deathzone_xyz4[0]+ catch_zone > robot_xyz[0])):
            return bool(1)
    return bool(0)

#death_text = death_zone.getField("MF_NODE")
while supervisor.step(TIME_STEP) != -1:
    # repeats with time step
    values1 = trans_field1.getSFVec3f()
    values2 = trans_field2.getSFVec3f()

    if simulationDone ==1:
        supervisor.simulationSetMode(Supervisor.SIMULATION_MODE_PAUSE)

    if robot_in_zone(values1, deathzone_xyz2, 0.4):
        os.system('echo \\n' + cont1str + ', ' + cont2str + ', 1 > ..\\..\\..\\UI\\public\\Tournament.txt')
        supervisor.setLabel(1, "robot 1 wins", 0.2, 0.2, 0.1, 000, 0, "Arial")
        supervisor.simulationQuit(1)
    if robot_in_zone(values2, deathzone_xyz1, 0.4):
        os.system('echo \\n' + cont1str + ', ' + cont2str + ', 2 > ..\\..\\..\\UI\\public\\Tournament.txt')
        supervisor.setLabel(1, "robot 2 wins", 0.2, 0.2, 0.1, 000, 0, "Arial")
        supervisor.simulationQuit(1)

    if Robot.getTime(supervisor) > 60:
        os.system('echo \\n' + cont1str + ', ' + cont2str + ', 4 > ..\\..\\..\\UI\\public\\Tournament.txt')
        supervisor.setLabel(1, "timeout", 0.2, 0.2, 0.1, 000, 0, "Arial")
        supervisor.simulationQuit(1)

    keypressed = keyboard.getKey()
    if keypressed == 32:
        if (1 == supervisor.simulationGetMode()):
            supervisor.simulationSetMode(Supervisor.SIMULATION_MODE_PAUSE)
        else:
            supervisor.simulationSetMode(1)
