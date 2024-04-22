import cozmo
from cozmo.objects import CustomObjectMarkers, CustomObjectTypes, CustomObject, LightCube, LightCube3Id,LightCube2Id
from .people import *
from .weapon import *



class Object_information():
    
    def __init__(self,object_type,position,object,is_cube=False):
        self.type = object_type
        self.pose = position
        self.is_cube = is_cube
        self.obj = object



type_marker_map = {
    CustomObjectTypes.CustomType01: CustomObjectMarkers.Hexagons3,
    CustomObjectTypes.CustomType02: CustomObjectMarkers.Diamonds5,
    CustomObjectTypes.CustomType03: CustomObjectMarkers.Triangles2,
    CustomObjectTypes.CustomType04: CustomObjectMarkers.Circles5,
    CustomObjectTypes.CustomType05: CustomObjectMarkers.Diamonds3,          
    CustomObjectTypes.CustomType06: CustomObjectMarkers.Hexagons4,
    CustomObjectTypes.CustomType07: CustomObjectMarkers.Circles2,
    CustomObjectTypes.CustomType08: CustomObjectMarkers.Diamonds4,
    CustomObjectTypes.CustomType09: CustomObjectMarkers.Circles3,
    CustomObjectTypes.CustomType10: CustomObjectMarkers.Triangles4,
    CustomObjectTypes.CustomType11: CustomObjectMarkers.Hexagons2,
    CustomObjectTypes.CustomType12: CustomObjectMarkers.Triangles3,
}

def get_object_type(objects_action_dict, obj) :
    
    if (isinstance(obj,CustomObject)) :
        return objects_action_dict[obj.object_type][1]
    elif (isinstance(obj,LightCube)):
        return objects_action_dict[obj][1]
    else:
        return None


    

def init_object_dict(robot) -> dict:
    objects_action = {}

    objects_action[CustomObjectTypes.CustomType01] = ((CustomObjectTypes.CustomType01,type_marker_map[CustomObjectTypes.CustomType01],55,25,25), Peopletype.Blanc)
    objects_action[CustomObjectTypes.CustomType02] = ((CustomObjectTypes.CustomType02,type_marker_map[CustomObjectTypes.CustomType02],55,25,25), Peopletype.Bleu)
    objects_action[CustomObjectTypes.CustomType03] = ((CustomObjectTypes.CustomType03,type_marker_map[CustomObjectTypes.CustomType03],55,25,25), Peopletype.Jaune) 
    objects_action[robot.world.get_light_cube(LightCube3Id)] = ((CustomObjectTypes.CustomType04,type_marker_map[CustomObjectTypes.CustomType04],55,25,25), Peopletype.Mauve) # a modifier
    objects_action[robot.world.get_light_cube(LightCube2Id)] = ((CustomObjectTypes.CustomType05,type_marker_map[CustomObjectTypes.CustomType05],55,25,25), Peopletype.Rouge) # a modifier
    objects_action[CustomObjectTypes.CustomType06] = ((CustomObjectTypes.CustomType06,type_marker_map[CustomObjectTypes.CustomType06],55,25,25), Peopletype.Vert)
    objects_action[CustomObjectTypes.CustomType07] = ((CustomObjectTypes.CustomType07,type_marker_map[CustomObjectTypes.CustomType07],55,25,25), WeaponType.Chandelier) 
    objects_action[CustomObjectTypes.CustomType08] = ((CustomObjectTypes.CustomType08,type_marker_map[CustomObjectTypes.CustomType08],55,25,25), WeaponType.Cle_anglaise)
    objects_action[CustomObjectTypes.CustomType09] = ((CustomObjectTypes.CustomType09,type_marker_map[CustomObjectTypes.CustomType09],55,25,25), WeaponType.Corde)
    objects_action[CustomObjectTypes.CustomType10] = ((CustomObjectTypes.CustomType10,type_marker_map[CustomObjectTypes.CustomType10],55,25,25), WeaponType.Matraque)
    objects_action[CustomObjectTypes.CustomType11] = ((CustomObjectTypes.CustomType11,type_marker_map[CustomObjectTypes.CustomType11],55,25,25), WeaponType.Poignard)
    objects_action[CustomObjectTypes.CustomType12] = ((CustomObjectTypes.CustomType12,type_marker_map[CustomObjectTypes.CustomType12],55,25,25), WeaponType.Revolver) 
    
    return objects_action


def update_world_objects(robot : cozmo.robot.Robot, new_obj_dict: dict):
    
    robot.world.undefine_all_custom_marker_objects()

    for object, data in new_obj_dict.items():
        check = robot.world.define_custom_cube(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4])
        if check is None:
            print("error defining object\n")
            return False

    return 

