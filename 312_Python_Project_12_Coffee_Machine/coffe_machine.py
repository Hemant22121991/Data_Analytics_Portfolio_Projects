MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

quarter = 0.25
dime  = 0.1
nickle = 0.05
penny = 0.01

profit = 0

def coffee_resources(res_dict):
    '''Prints the current resources and profit.'''
    for key,value in res_dict.items():
        print(f"{key} : {value}")
    print(f"Money: ${profit}")

def resource_check(res_dict,u_input):
    '''Checks if resources are sufficient. Returns missing resource or None.'''
    required = MENU[u_input]["ingredients"]
    for resource in ["water", "milk", "coffee"]:
        if res_dict[resource] < required[resource]:
            return resource
    return None

def coffee_machine():

    global profit
    main_dict = resources
    user_input = input("What would you like?(espresso/latte/cappuccino): ").lower()

    if user_input == 'off':
        return 20 #Signal to turn off
    elif user_input == 'report':
        coffee_resources(main_dict)
        return
    elif user_input not in MENU:
        print("Invalid choice. Please try again.")
        return # Continue loop
    
    # Check resources

    missing_resource = resource_check(main_dict,user_input)
    if missing_resource:
        print(f"Sorry, there's not enough {missing_resource}.")
        return
    
    #process coins

    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return
    
    total = (
        quarters * quarter
        + dimes * dime
        + nickles * nickle
        + pennies * penny
    )

    cost = MENU[user_input]["cost"]

    if total < cost:
        print ("Sorry that's not enough money. Money refunded.")
        return
    else:
        profit = profit + cost
        change = total - cost
        if change > 0:
            print(f"Here is ${round(change,2)} in change.")
        print(f"Here your ☕ {user_input}. Enjoy!")  

    # Deduct resources    
    for resource in ["water", "milk", "coffee"]:
        main_dict[resource] -= MENU[user_input]["ingredients"][resource]

#Main Loop
machine_on = True
while machine_on:
    check = coffee_machine()
    if check == 20:
        machine_on = False