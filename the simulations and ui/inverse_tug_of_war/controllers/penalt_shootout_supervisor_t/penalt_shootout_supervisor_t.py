from controller import Supervisor, Keyboard
import sys, os

TIME_STEP = 64

supervisor = Supervisor()
keyboard = Keyboard()

keyboard.enable(10)

robot_node1 = supervisor.getFromDef("ROBOT_1")
robot_node2 = supervisor.getFromDef("ROBOT_2")
football_node = supervisor.getFromDef("football")
goal_node = supervisor.getFromDef("goal")

trans_field1 = robot_node1.getField("translation")
trans_field2 = robot_node2.getField("translation")
trans_field3 = football_node.getField("translation")
trans_field4 = goal_node.getField("translation")
robot1cont = robot_node1.getField("controller")
robot2cont = robot_node2.getField("controller")
cont1str = robot1cont.getSFString()
cont2str = robot2cont.getSFString()

simulationDone = 0

goal_xyz = trans_field4.getSFVec3f()

def robot_in_zone (robot_xyz, zone_xyz, zone_size):
    catch_zone = zone_size/2
    if ((zone_xyz[2]- catch_zone < robot_xyz[2])and(zone_xyz[2]+ catch_zone > robot_xyz[2])):
        if ((zone_xyz[0]- catch_zone < robot_xyz[0])and(zone_xyz[0]+ catch_zone > robot_xyz[0])):
            return bool(1)
    return bool(0)

def football_in_zone (football_xyz, zone_xyz, zone_size):
    catch_zone = zone_size/2
    if ((zone_xyz[2] > football_xyz[2])):
        if ((zone_xyz[0]- catch_zone < football_xyz[0])and(zone_xyz[0]+ catch_zone > football_xyz[0])):
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
    football_xyz = trans_field3.getSFVec3f()

    if simulationDone ==1:
        supervisor.simulationSetMode(Supervisor.SIMULATION_MODE_PAUSE)

    if football_in_zone(football_xyz, goal_xyz, 2):
        supervisor.setLabel(1, "goal", 0.2, 0.2, 0.1, 000, 0, "Arial")
        #supervisor.worldReload()

    keypressed = keyboard.getKey()
    if keypressed == 32:
        if (1 == supervisor.simulationGetMode()):
            supervisor.simulationSetMode(Supervisor.SIMULATION_MODE_PAUSE)
        else:
            supervisor.simulationSetMode(1)
