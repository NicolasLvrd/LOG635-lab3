import os
os.environ['PYOPENGL_PLATFORM'] = 'glx'

from .map.map import place_walls
from .map.object import update_world_objects, init_object_dict, get_object_type, Object_information
from .map.room import RoomType

import cozmo
from cozmo.objects import ObservableObject, LightCube, EvtObjectTapped, CustomObject
from cozmo.util import Pose

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

    robot.roll_cube(victim.obj,num_retries=2).wait_for_completed()


def answer_by_tap(robot):
    time_out = False
    cpt = 0

    while (not time_out) :
        try: 
            tap = robot.wait_for(EvtObjectTapped,timeout=3)
            print(tap)
        except Exception as e:
            time_out = True
            break

        cpt += tap.tap_count

    print(cpt)

    return cpt == 1 




def cozmo_program(robot: cozmo.robot.Robot):
    objects = init_object_dict(robot)

    # # set objects in the world
    update_world_objects(robot,objects)
    
    # # set walls 
    # place_walls(robot)

    f = look_for_information(robot,objects)


    roll_victim(robot,f[0])

    # print(answer_by_tap(robot))







cozmo.run_program(cozmo_program, use_3d_viewer=True)
