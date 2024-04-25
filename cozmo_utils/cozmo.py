import os
from time import sleep
os.environ['PYOPENGL_PLATFORM'] = 'glx'

from .map.map import place_walls
from .map.object import update_world_objects, init_object_dict, get_object_type, Object_information
from .map.room import RoomType

import cozmo
from cozmo.objects import ObservableObject, LightCube, EvtObjectTapped, CustomObject, LightCube2Id
from cozmo.util import Pose, degrees

def look_for_information(robot,world_objects):
    
    object_found = []

    obj_list = []
    
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    obj_list = robot.world.wait_until_observe_num_objects(num=2, object_type=ObservableObject, timeout=60)
    lookaround.stop()


    for obj in obj_list:
        
        if (isinstance(obj,LightCube) or isinstance(obj,CustomObject)):

            object_type = get_object_type(world_objects,obj)

            info = Object_information(object_type,obj.pose,obj)
            if (isinstance(obj,LightCube)):
                info.is_cube = True

            object_found.append(info)


    return object_found


def roll_victim(robot,victim:Object_information):

    robot.go_to_object(victim.obj,cozmo.util.Distance(distance_mm=100)).wait_for_completed()

    e = robot.roll_cube(victim.obj,num_retries=1).wait_for_completed()

    # print(e)
    



def answer_by_tap(robot):
    time_out = False
    cpt = 0

    while (not time_out) :
        try: 
            tap = robot.wait_for(EvtObjectTapped,timeout=3)
            # print(tap
        except Exception as e:
            time_out = True
            break

        cpt += tap.tap_count


    return cpt == 1 

def justice(robot):
    lightcube =  robot.world.get_light_cube(LightCube2Id)
    
    e = robot.go_to_object(lightcube,cozmo.util.Distance(distance_mm=100)).wait_for_completed()
    print(e)

    e = robot.pickup_object(lightcube,num_retries= 2).wait_for_completed()
    print(e)

    robot.go_to_pose(Pose(0,0,0,angle_z=degrees(0))).wait_for_completed()

    robot.place_object_on_ground_here(lightcube,num_retries=2).wait_for_completed()



def cozmo_program(robot: cozmo.robot.Robot):
    objects = init_object_dict(robot)

    # # set objects in the world
    update_world_objects(robot,objects)
    
    # # set walls 
    # place_walls(robot)

    # f = look_for_information(robot,objects)


    # roll_victim(robot,f[0])


    justice(robot)

    # print(answer_by_tap(robot))




if __name__ == "__main__":
    cozmo.run_program(cozmo_program, use_3d_viewer=True)
