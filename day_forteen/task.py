import random
from data import data
from art import logo , vs
def compare_data(player_a,player_b,vs):
    print(f"compare A : {player_a['name']}, a {player_a['description']} , from {player_a['country']}")
    print(vs)
    print(f"Against B : {player_b['name']}, a {player_b['description']} , from {player_b['country']}")
    answer=input("who has more followers? type A OR B\n").lower()
    answer_control= True if player_a['follower_count'] > player_b['follower_count'] else False
    return answer , answer_control
def increase_score(player_a,player_b,score):
    score +=1
    print(f"your are right, current score is : {score}")
    player_a=player_b
    player_b=random.choice(data)
    data.remove(player_b)
    return player_a,player_b,score
def main():
    score=0
    print(logo)
    player_a=random.choice(data)
    data.remove(player_a)
    player_b=random.choice(data)
    data.remove(player_b)
    while True: 
        answer, answer_control=compare_data( player_a,player_b,vs)
        if answer == "a" : 
            if answer_control:
                player_a,player_b,score=increase_score(player_a,player_b,score)
            else : 
                print(f"unfortunately you are wrong, your final score is : {score}")
                break
        elif answer == "b" : 
            if not answer_control:
                player_a,player_b,score=increase_score(player_a,player_b,score)
            else : 
                print(f"unfortunately you are wrong, your final score is : {score}")
                break
        else : print("Invalid value , type correct answer (A or B)")


if __name__=="__main__":
    main()