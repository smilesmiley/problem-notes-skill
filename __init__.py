from mycroft import MycroftSkill, intent_file_handler
from datetime import datetime
import json
import os
import time

class ProblemNotes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.questions = {1: "What problem occured to you?",
                          2: "When exactly did the problem occur?",
                          3: "Do you want to describe it further? Or do you want to note down something else?"
                          }

    @intent_file_handler('notes.problem.intent')
    def handle_notes_problem(self, message):
        self.speak_dialog('notes.problem')
        time.sleep(1)
        self._ask_all_questions()

    def _ask_user(self, number,question, timestamp):
        # asks question
        answer = self.ask_yesno(question)
        # saves audio
        src = os.path.join(os.path.abspath('..'), 'study_data', 'audio', 'audio_file_user.wav')
        dest = os.path.join(os.path.abspath('..'), 'study_data', 'problems', 'audio',
                            timestamp + "_question_" + str(number) + ".wav")
        os.rename(src, dest)
        return answer

    def _ask_all_questions(self):
        survey = []
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        for i in range(1, len(self.questions)+1):
            question = self.questions[i]
            answer = self._ask_user(i,question, timestamp)
            survey.append(('diary', question, answer, timestamp))
        # saves question,answer, skill instance in a json file
        with open(os.path.join(os.path.abspath('..'), 'study_data', 'problems', 'json', timestamp + 'log_file_ours.json'),
                  'w') as f:
            json.dump(survey, f, indent=4, sort_keys=True)

def create_skill():
    return ProblemNotes()

