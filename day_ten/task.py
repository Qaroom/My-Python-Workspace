offer_dict={}
offer_values=[]
offers_name=[]

def main():
    print("Welcome to the secret auction program :))\n")
    person_name=input("type your name : \n")
    person_offer=int(input("enter your offer : \n"))
    offer_dict[person_name]=person_offer
  
    while True:
        control_param=input("DO you want to give anthor offer ?(y/n)\n").lower()
        if control_param == "y":
            person_name=input("type your name : \n")
            person_offer=int(input("enter your offer : \n"))
            offer_dict[person_name]=person_offer

        elif control_param =="n":
            if len(offer_dict)==0: 
                print("There is not any offer, please enter any offer")
            
            else : 
                for offer in offer_dict: 
                    offer_values.append(offer_dict[offer])
                    offers_name.append(offer)
                
                #or (max_offer_name=max(offer_dict,key=offer_dict.get))

                max_offer_index=offer_values.index(max(offer_values))
                max_offer_name=offers_name[max_offer_index]
                print(f"The winner of secret auction program is {max_offer_name}, congratulaiton\n")
                print(f"the offer was : {offer_dict[max_offer_name]}")

            break
        else : 
            print("type current value, y or n !!! \n")


if __name__=="__main__":
    main()