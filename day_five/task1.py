# import random

# fruits=["Apple","Peach","Pear"]


# student_number=30

# student_score=[]
# a=random.randint(40, 100)
# print(a)
# total=0
# for i in range(student_number):
#     student_score.append(round(random.uniform(40, 100),2))



# print(student_score)
# print(sum(student_score))

# for i in student_score :
#     total+=i


# print(total)
# min_score=min(student_score)
# print(min_score)
# print(student_score.index(min_score))


# a=int(input("toplanmasi gereken sayi giriniz"))

# toplam=(a+1)*(a/2)

# print(int(toplam))
# toplam=0
# for number in range(1,a+1): 
#     toplam+=number

# print(toplam)

# print(5%3)

# for number in range(1,101):
#     fizz_control=number%3
#     buzz_control=number%5

#     if fizz_control == 0 and buzz_control == 0:
#         print("FizzBuzz")

#     elif fizz_control == 0 :
#         print("Fizz")
#     elif buzz_control == 0 : 
#         print("Buzz")
#     else :
#         print(number)

import random
password_list=[]

letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number=[0,1,2,3,4,5,6,7,8,9]

symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','"',"'",'<',',','>','.','?','/']

number_of_letter=int(input("How many letter do you need in your password:=?"))
number_of_number=int(input("How many number do you need in your password:=?"))
number_of_symbol=int(input("How many symbol do you need in your password:=?"))

for char in  range(1,number_of_letter+1):
    char_letter=random.choice(letter)
    password_list.append(char_letter)
    letter.remove(char_letter)


for sym in  range(1,number_of_symbol+1):
    sym_letter=random.choice(symbols)
    password_list.append(sym_letter)
    symbols.remove(sym_letter)


for num in  range(1,number_of_number+1):
    num_letter=random.choice(number)
    number.remove(num_letter)
    password_list.append(str(num_letter))
    
random.shuffle(password_list)
final_password = ''.join(password_list)
print(f"Your Password is : {final_password}")