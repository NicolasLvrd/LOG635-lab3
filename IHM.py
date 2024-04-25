import cozmo
import voice_to_text 
import cozmo_utils.cozmo as cutils

def ask_text(robot: cozmo.robot.Robot, text: str):
    tmp = robot.say_text(text).wait_for_completed()

    output = prompt_text(text)

    return output


def prompt_text(text: str):

    output = input("[Cozmo] : " + text + "\n>>> ")

    if "VOICE" in output:
        voice_to_text.enregistrer_audio("enregistrement.wav", 5)
        output = voice_to_text.speech_recognition("enregistrement.wav")
        # print(output)
    
    print("\n\n")

    return output

def ask_yes_no(robot: cozmo.robot.Robot, text: str):
    tmp = robot.say_text(text).wait_for_completed()

    print("[Cozmo] : " + text + "  (réponse par tapotement)")

    output = cutils.answer_by_tap(robot)

    print(">>> " + "oui" if output else "non"   + "\n\n")

    return output

def show_thought(robot: cozmo.robot.Robot, text: str):
    
    # print text in italics and in color orange
    print("\033[3;36m[Cozmo](pense que) " + text + "\033[0m")

