import random

words = [
    "apple", "car", "book", "table", "pencil",
    "phone", "window", "cloud", "ocean", "mountain",
    "flower", "star", "dog", "sun", "wind"
]
control_world=random.choice(words)
desired_word=list(control_world)
empty_word=["_" for i in range(len(desired_word))]

your_chance=3
def world_filled():
    pass

while world_filled: 
    entered_char=input("Enter One alphabet : \n")

    if entered_char in desired_word:
        char_index=desired_word.index(entered_char) 
        empty_word[char_index]=entered_char
        desired_word[char_index]="_"
    
    elif entered_char not in desired_word:
        if your_chance == 0:
            print("yor lose all your")
            break 
        your_chance-=1
        print("////////////////////////////")
        print(f"{your_chance} chance remain")
        print("////////////////////////////")

    final_world=''.join(empty_word)
    print("####################\n",final_world,"\n","####################")
    

    if final_world ==control_world:
        print("Conguratalation, you win")
        break
    


# word="akram"
# x="m"
# print(word.index(x))