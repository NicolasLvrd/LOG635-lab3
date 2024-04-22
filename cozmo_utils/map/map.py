from time import sleep
import cozmo
from cozmo.util import degrees, Pose
from .room import RoomType, go_to_room



def place_walls(robot: cozmo.robot.Robot):

    # ext

    # ext 1
    x = 0
    y = 400
    len = 800
    fixed_object = robot.world.create_custom_fixed_object(Pose(x+len/2, y, 0, angle_z=degrees(90)),
                                                        10, len, 100, relative_to_robot=False)
    if fixed_object:
        print("ext 1 created successfully")
    # ext 2
    x = 800
    y = 400
    len = 800
    fixed_object = robot.world.create_custom_fixed_object(Pose(x, y-len/2, 0, angle_z=degrees(0)),
                                                        10, len, 100, relative_to_robot=False)
    if fixed_object:
        print("ext2 created successfully")
    # ext 3
    x = 0
    y = -400
    len = 800
    fixed_object = robot.world.create_custom_fixed_object(Pose(x+len/2, y, 0, angle_z=degrees(90)),
                                                        10, len, 100, relative_to_robot=False)
    if fixed_object:
        print("ext 3 created successfully")
    # ext 4
    x = 0
    y = -100
    len = 300
    fixed_object = robot.world.create_custom_fixed_object(Pose(x, y-len/2, 0, angle_z=degrees(0)),
                                                        10, len, 100, relative_to_robot=False)
    if fixed_object:
        print("ext 4 created successfully")
    # ext 5
    x = 0
    y = 400
    len = 300
    fixed_object = robot.world.create_custom_fixed_object(Pose(x, y-len/2, 0, angle_z=degrees(0)),
                                                        10, len, 100, relative_to_robot=False)
    if fixed_object:
        print("ext 5 created successfully")


    # Salon

    # 1
    x = 0
    y = 100
    len = 100
    fixed_object = robot.world.create_custom_fixed_object(Pose(x+len/2, y, 0, angle_z=degrees(90)),
                                                        10, len, 100, relative_to_robot=False)
    if fixed_object:
        print("1 created successfully")

    # 2
    x = 200
    y = 100
    len = 200
    fixed_object = robot.world.create_custom_fixed_object(Pose(x+len/2, y, 0, angle_z=degrees(90)),
                                                        10, len, 100, relative_to_robot=False)
    if fixed_object:
        print("2 created successfully")

    # 10
    x = 300
    y = 400
    len = 300
    fixed_object = robot.world.create_custom_fixed_object(Pose(x, y-len/2, 0, angle_z=degrees(0)),
                                                        10, len, 100, relative_to_robot=False)
    if fixed_object:
        print("10 created successfully")


    # Bureau

    # 3
    x = 500
    y = 100
    len = 100
    fixed_object = robot.world.create_custom_fixed_object(Pose(x+len/2, y, 0, angle_z=degrees(90)),
                                                        10, len, 100, relative_to_robot=False)
    if fixed_object:
        print("3 created successfully")

    # Galerie

    # 7
    x = 600
    y = 400
    len = 350
    fixed_object = robot.world.create_custom_fixed_object(Pose(x, y-len/2, 0, angle_z=degrees(0)),
                                                        10, len, 100, relative_to_robot=False)
    if fixed_object:
        print("7 created successfully")

    # 8
    x = 600
    y = -50
    len = 350
    fixed_object = robot.world.create_custom_fixed_object(Pose(x, y-len/2, 0, angle_z=degrees(0)),
                                                        10, len, 100, relative_to_robot=False)
    if fixed_object:
        print("8 created successfully")


    # Salle a manger

    # 4
    x = 500
    y = -100
    len = 100
    fixed_object = robot.world.create_custom_fixed_object(Pose(x+len/2, y, 0, angle_z=degrees(90)),
                                                        10, len, 100, relative_to_robot=False)
    if fixed_object:
        print("4 created successfully")



    # Cuisine

    # 6
    x = 0
    y = -100
    len = 100
    fixed_object = robot.world.create_custom_fixed_object(Pose(x+len/2, y, 0, angle_z=degrees(90)),
                                                        10, len, 100, relative_to_robot=False)
    if fixed_object:
        print("6 created successfully")

    # 5
    x = 200
    y = -100
    len = 200
    fixed_object = robot.world.create_custom_fixed_object(Pose(x+len/2, y, 0, angle_z=degrees(90)),
                                                        10, len, 100, relative_to_robot=False)
    if fixed_object:
        print("5 created successfully")

    # 9
    x = 300
    y = -100
    len = 300

    fixed_object = robot.world.create_custom_fixed_object(Pose(x, y-len/2, 0, angle_z=degrees(0)),
                                                        10, len, 100, relative_to_robot=False)
    if fixed_object:
        print("9 created successfully")






if __name__ == "__main__":
    import os
    os.environ['PYOPENGL_PLATFORM'] = 'glx'


    def cozmo_program(robot: cozmo.robot.Robot):
        place_walls(robot)


        for r in Room:
            go_to_room(robot,r)

            look_for_information(robot)


            sleep(1)


    cozmo.run_program(cozmo_program, use_3d_viewer=True)
