import random
import art
print(art.logo)
def decrease_attempts(attempts):
    attempts-=1
    print(f"You have {attempts} remaining to guess the number")
    return attempts
def number_control(number_range):
    num=int(input("Make a guess"))
    if num > number_range:
        print("Too high")
        return False
    elif num < number_range:
        print("Too low")
        return False
    else : 
        print(f"You got it, The answer was {number_range}")
        return True

def main():
    game_level=input("Choose a difficulty. Type 'hard' or 'easy'").lower()
    game_attempts= 5 if game_level=="hard" else 10
    print(f"you got {game_attempts} atempts")
    number_range=random.randint(0,100)
    while True: 
        atemp_control=number_control(number_range)
        if atemp_control == True:
            break
        else :
            game_attempts=decrease_attempts(game_attempts)
            if game_attempts ==0:
                print(f"you lost all your attempt,Right answer was {number_range}")
                break
            else:
                pass

if __name__=="__main__":
    main()