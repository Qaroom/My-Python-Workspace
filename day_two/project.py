total_of_bill=float(input("what was the total bill ?"))
total_of_tip=float(input("how much tiip would you like to give ?"))
total_of_people=float(input("how many people to split the bill?"))

final_bill=((total_of_bill+total_of_tip)/total_of_people)

print(f"Each person should pay : {round(final_bill,2)}")