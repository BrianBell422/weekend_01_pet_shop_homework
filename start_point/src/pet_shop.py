# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash
    return pet_shop["admin"]["total_cash"]

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] += pets_sold
    return pet_shop["admin"]["pets_sold"]

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# def get_pets_by_breed(pet_shop, breed):
#     return [pet for pet in pet_shop['pets'] if pet['breed'] == breed]

def get_pets_by_breed(pet_shop, breed):
    pet_search = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pet_search.append(pet)
    return pet_search

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet


def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_to_remove = pet
    pet_shop["pets"].remove(pet_to_remove)


def add_pet_to_stock(pet_shop, new_pet_add):
    new_pet_to_add = new_pet_add
    pet_shop["pets"].append(new_pet_to_add)

# def add_pet_to_stock(pet_shop, new_pet_add):
#     new_pet_to_add = new_pet_add
#     for pet in new_pet_add:
#         if pet in new_pet_add == True:
#             new_pet_to_add = pet
#     pet_shop["pets"].append(new_pet_to_add)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, cash_rem):
    customer["cash"] -= cash_rem
    return customer["cash"]


def get_customer_pet_count(customer):
    customer_pets = customer["pets"]
    return len(customer_pets)


def add_pet_to_customer(customer, new_pet_add):
    new_pet_to_add = new_pet_add
    customer["pets"].append(new_pet_to_add)


# OPTIONAL

def customer_can_afford_pet (customer, new_pet):
    cust_cash = get_customer_cash(customer)
    pet_cost = new_pet["price"]
    if cust_cash >= pet_cost:
        return True
    else:
        return False


def sell_pet_to_customer (pet_shop, pet, customer):
    cust_pet_count = get_customer_pet_count(customer)
    pets_sold = get_pets_sold(pet_shop)
    cust_cash = get_customer_cash(customer)
    shop_total_cash = get_total_cash(pet_shop)



        



    


        
            


            
            
            
