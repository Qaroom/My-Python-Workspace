# # import turtle
# # import prettytable

# # dimmy=turtle.Turtle()
# # dimmy.shape("turtle")
# # dimmy_screen=turtle.Screen()
# # print(dimmy.color)
# # dimmy_screen.exitonclick()

# from prettytable import PrettyTable
# import prettytable

# table=PrettyTable()
# table.add_column("pokemon name",["x","a","b"])
# table.add_column("Type",["x","a","b"])

# print(table)
from coffee_class import CoffeeMechine
coffee=CoffeeMechine()
def main():
    profits=[]
    while True: 
        drink=input("What would you lik (espresso | latte | cappuccino)")
        if drink == "off":
            print("Coffee mechine has been closed")
            break
        elif drink =="report":
            totoal_profits=sum(profits)
            coffee.update_money(totoal_profits)
            coffee.print_list_keys(coffee.resources)
            continue
        
        check_resource=coffee.check_resources(coffee.menu[drink])
        cost=coffee.menu[drink]["cost"]
        if check_resource : 
            check_money,profit= coffee.insert_and_check_money(cost)
            if check_money: 
                print(f"your {drink} is ready , enjoy your drink")
                profits.append(profit)
                new_resources=coffee.update_resources(coffee.menu[drink])
                coffee.resources=new_resources
            else : 
                continue
        
        else : 
            print("we just have only this resources values :")
            coffee.print_list_keys(coffee.resources)
        

if __name__=="__main__":
    main()
 