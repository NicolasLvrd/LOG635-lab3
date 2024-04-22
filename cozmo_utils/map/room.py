
from enum import Enum
import cozmo
from cozmo.util import degrees, Pose


class RoomType(Enum):
    Hall = ("hall",(300,0,degrees(0)))
    Bureau = ("bureau",(450,200,degrees(90)))
    Salon = ("salon",(150,200,degrees(90)))
    Cuisine = ("cuisine",(150,-200,degrees(-90)))
    Chambre = ("chambre",(450,-200,degrees(-90)))
    Galerie = ("galerie",(700,0,degrees(-90)))


def go_to_room(robot:cozmo.robot.Robot,room :RoomType):
    val = room.value[1]
    robot.go_to_pose(Pose(val[0], val[1], 0, angle_z=val[2]), relative_to_robot=False).wait_for_completed()
