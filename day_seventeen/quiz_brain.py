
class QuizBrain:
    def __init__(self,questions):
        self.question_index=0
        self.questions_list=questions

    def still_has_question(self):
        if self.question_index == len(self.questions_list):
            return False
        else :
            return True

    def next_question(self):
        
            self.answer=input(f"{self.question_index+1}.Q : {self.questions_list[self.question_index].question} (True or False)").lower()
            self.question_index+=1


    def check_answer(self):
         if self.answer == self.questions_list[self.question_index-1].answer:
              return True
         else :
              return False

        