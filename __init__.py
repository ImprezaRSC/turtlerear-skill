from mycroft import MycroftSkill, intent_file_handler
import subprocess

class Turtlerear(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('turtlerear.intent')
    def handle_turtlerear(self, message):
        self.speak_dialog('turtlerear')
        s = "rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[-2.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]'"
        subprocess.call([s],shell=True)

def create_skill():
    return Turtlerear()

