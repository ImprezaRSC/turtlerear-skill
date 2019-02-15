from mycroft import MycroftSkill, intent_file_handler


class Turtlerear(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('turtlerear.intent')
    def handle_turtlerear(self, message):
        self.speak_dialog('turtlerear')


def create_skill():
    return Turtlerear()

