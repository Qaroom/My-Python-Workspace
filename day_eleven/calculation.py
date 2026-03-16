# calculation_symbol = """
#     _____________________
# |  _________________  |
# | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
# | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
# |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
# | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
# | |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
# | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |
# | |___|___|___| |___| | | |  \\ '.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ '.___.'\\  | |
# | | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
# | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
# | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
# | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
# |_____________________|
# """

# print(calculation_symbol)

# def operation(n1,n2,operation_symbol):
#     if operation_symbol == "/":
#         return n1/n2
#     elif operation_symbol == "*" :
#         return n1 * n2
   
#     elif operation_symbol == "-" :
#         return n1 - n2
   
#     elif operation_symbol == "+" :
#         return n1 + n2
   
#     else :
#         print("invalid operation symbol!!!")
#         return
   
       
       

# def main():
#     n1=int(input("Enter first number : \n"))
#     operation_symbol=input("enter operation symbol : / * - +\n")
   
#     n2=int(input("Enter second number : \n"))
   
#     result=operation(n1,n2,operation_symbol)
#     print(result)
   
#     while True :
#         next_operation_type=input("Press 'n' to new operation or 'c' to continue with previous  operation's result or 'q' to exiting\n")
#         if next_operation_type == "n":
#             n1=int(input("Enter first number : \n"))
#             operation_symbol=input("enter operation symbol : / * - +")
           
#             n2=int(input("Enter second number : \n"))
           
#             result=operation(n1,n2,operation_symbol)
#             print(result)
           
#         elif next_operation_type == "c" :
#             n1=result
#             operation_symbol=input("enter operation symbol : / * - +")
           
#             n2=int(input("Enter second number : \n"))
           
#             result=operation(n1,n2,operation_symbol)
#             print(result)
           
#         elif next_operation_type == "q":
#             print("Thank you for use my caculation, have a nice day")
#             break
#         else :
#             print("invalid entry, make sure you type the currect symbol")
   
   

# if __name__=="__main__":
#     main()





calculation_symbol = """Calculator"""
print(calculation_symbol)


def operation(n1, n2, op):
    operations = {
        "+": n1 + n2,
        "-": n1 - n2,
        "*": n1 * n2,
        "/": n1 / n2 if n2 != 0 else "Division by zero!"
    }
    return operations.get(op, "Invalid operation")


def get_input():
    n1 = float(input("Enter first number: "))
    op = input("Enter operation (+ - * /): ")
    n2 = float(input("Enter second number: "))
    return n1, op, n2


def main():
    n1, op, n2 = get_input()
    result = operation(n1, n2, op)
    print("Result:", result)

    while True:
        choice = input("n=new | c=continue | q=quit: ")

        if choice == "q":
            print("Thanks for using the calculator 👋")
            break

        if choice == "n":
            n1, op, n2 = get_input()

        elif choice == "c":
            op = input("Enter operation (+ - * /): ")
            n2 = float(input("Enter second number: "))
            n1 = result

        else:
            print("Invalid option")
            continue

        result = operation(n1, n2, op)
        print("Result:", result)


if __name__ == "__main__":
    main()
