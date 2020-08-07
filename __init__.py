from mycroft import MycroftSkill, intent_file_handler


class ProblemNotes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('notes.problem.intent')
    def handle_notes_problem(self, message):
        self.speak_dialog('notes.problem')


def create_skill():
    return ProblemNotes()

