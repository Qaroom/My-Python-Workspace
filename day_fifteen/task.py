from coffee_data import resources,menu,coins

def check_resources(drink):
    drink_list=drink["ingredients"]
    print(drink_list)
    for key in drink_list: 
        if drink_list[key] <= resources[key]:
            continue
        else : 
            print(f"sorry, there is not enough {key}")
            return False
    return True

def print_list_keys(list):
    for key in list : 
        print(f"{key} : {list[key]}")

def update_resources(resources,drink_list):
    drink_list=drink_list["ingredients"]
    new_resources={}
    for key in resources: 
        new_resources[key]= resources[key]-drink_list[key]

    return new_resources


def insert_and_check_money(coins,cost):
    total_inserted_money=0.0
    while True: 
        coin_type=input("Insert coins (q:0.25 | d:0.10 | n:0.05 | p:0.01) or enough \n").lower()
        if coin_type != "enough": 
            total_inserted_money+=coins[coin_type]
        else :
            if total_inserted_money >= cost:
                remained_money=total_inserted_money - cost 
                if remained_money > 0:
                    print(f"{remained_money} $ has been refunded")
                    total_inserted_money-=remained_money
                    return True , total_inserted_money
                else : 
                    return True  ,total_inserted_money 
            else : 
                print(f"sory that is not enough money, {total_inserted_money} $  refunded")
                return False ,total_inserted_money


def main():
    global resources
    profits=[]
    while True: 
        drink=input("What would you lik (espresso | latte | cappuccino)")
        if drink == "off":
            print("Coffee mechine has been closed")
            break
        elif drink =="report":
            totoal_profits=sum(profits)
            resources["Money"]=totoal_profits
            print_list_keys(resources)
            continue
        
        check_resource=check_resources(menu[drink])
        cost=menu[drink]["cost"]
        if check_resource : 
            check_money,profit= insert_and_check_money(coins,cost)
            if check_money: 
                print(f"your {drink} is ready , enjoy your drink")
                profits.append(profit)
                new_resources=update_resources(resources,menu[drink])
                resources=new_resources
            else : 
                continue
        
        else : 
            print("we just have only this resources values :")
            print_list_keys(resources)
        

if __name__=="__main__":
    main()