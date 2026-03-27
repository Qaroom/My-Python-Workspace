from question_data import quiz
from quiz_brain import QuizBrain
class Question:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer

questions = []
score=0
for q in quiz: 
    q_text=q["question"]
    a_text=q["answer"]
    new_q=Question(q_text,a_text)
    questions.append(new_q)


quiz1=QuizBrain(questions)
while True:
    if quiz1.still_has_question():
        quiz1.next_question()

    else : 
        print("There are no question left")
        break
    if quiz1.check_answer():
        score+=1
        print(f"your score is : {score}")

    else : 
        print(f"your are not right, your final score : {score}")
        break













            




# for i,question in enumerate(questions.values()):
#     print(f"{i+1}.Question{question.question} | {i+1}.answer{question.answer}")




# for i, question in enumerate(questions.values()):
#     print(f"{i+1}. Question: {question.question} | Answer: {question.answer}")



# class User:
#     def __init__(self,user_id,user_name):
#         self.id=user_id
#         self.name=user_name
#         self.followers=0
#         self.following=0
    
#     def follow(self,user):
#         user.followers+=1
#         self.following+=1



# user1=User("001","karoom")
# user2=User("002","angela")

# user1.follow(user2)
# print(user1.followers)
# print(user1.following)
# print(user2.followers)
# print(user2.following)
