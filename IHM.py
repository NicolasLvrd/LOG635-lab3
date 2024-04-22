import cozmo

def ask_text(robot: cozmo.robot.Robot, text: str):
    tmp = robot.say_text(text).wait_for_completed()

    output = prompt_text(text)

    return output


def prompt_text(text: str):

    output = input("[Cozmo] : " + text + "\n>>> ")

    print("\n\n")

    return output



def show_thought(robot: cozmo.robot.Robot, text: str):
    
    # print text in italics
    print("[Cozmo](pense que) \033[3m" + text + "\033[0m")