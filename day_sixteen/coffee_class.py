from coffee_data import resources,menu,coins

class CoffeeMechine:
    
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.coins={
            "q": 1.25,
            "d": 0.10,
            "n": 0.05,
            "p": 0.01

            }
        self.menu=menu
    def check_resources(self,drink):
        drink_list=drink["ingredients"]
        print(drink_list)
        for key in drink_list: 
            if drink_list[key] <= self.resources[key]:
                continue
            else : 
                print(f"sorry, there is not enough {key}")
                return False
        return True
    
    def print_list_keys(self,list):
        for key in list : 
            print(f"{key} : {list[key]}")
        
    def update_money(self,money):
        
        self.resources["money"]= money

    def update_resources(self,drink_list):
        drink_list=drink_list["ingredients"]
        # new_resources={}
        for key in self.resources: 
            self.resources[key]= self.resources[key]-drink_list[key]

        # return new_resources


    def insert_and_check_money(self,cost):
        total_inserted_money=0.0
        while True: 
            coin_type=input("Insert coins (q:0.25 | d:0.10 | n:0.05 | p:0.01) or enough \n").lower()
            if coin_type != "enough": 
                total_inserted_money+=self.coins[coin_type]
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

















