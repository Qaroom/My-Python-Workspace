try: 
    score=int(input("type your score in High school:\n"))
except ValueError: 
    print("Invalid valaue, you need to type a numrical number exm : 12")
    score=int(input("type your score in High school:\n"))

print (score)
