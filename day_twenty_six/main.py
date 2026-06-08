# range_list=range(1,5)
# new_list=[num+1 for num in range_list]
# print(new_list)

# names_list=["akram","mohammed","angella","lara", "poncik"]

# captil_names=[name.upper() for name in names_list if len(name)>5]
# print(captil_names)

import pandas


data=pandas.read_csv("C:/Users/mertc/Desktop/akram_stajyer_/python/My-Python-Workspace/day_twenty_six/nato_phonetic_alphabet.csv")
# print(data)

alphapet_code_dict={rows.letter:rows.code for (index,rows) in data.iterrows()}
# print(alphapet_code_dict)
while True:
        
    name=str(input("Type name with you need to get its code: \n")).upper()
    if name=="E":
        break
    name_code_list=[alphapet_code_dict[f"{letter}"] for letter in name if letter!=" "]

    print(name_code_list)
