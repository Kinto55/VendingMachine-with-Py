# Return an empty list if no items are found in the vending machine

"""
-- We have the items list which has nested python dictionaries. 
-- As you can see, each item has 3 keys: name, code and price. 
-- You can add more food items to this list if you want but make sure you add the code and price as well. 
"""
items = [
    {
        # Returns a list of all the possible values for the code.
        "code": 0,
        # Returns the name of the class.
        "name": "coca cola",
        "price": 5,
    },
    {
        # Returns a list of all the data in the database.
        # Returns the code of the first line of the line.
        "code": 1,
        # Returns the name of the cadbury.
        "name": "cadbury",
        # The price of the item.
        "price": 10,
    },
    {
        # Returns a list of chips and price strings.
        "code": 2,
        "name": "chips",
        "price": 2,
    },
]

"""
--Then we have the while loop which runs till the variable is_quit becomes true.
-- This allows the program to run as long as the user wants to quit.
            """
is_quit = False
item = ""

# Welcome to the vending machine
while not is_quit:
    print("Welcome to the vending machine")
    # Print items to stdout.
    for i in items:
        print(f"Item Name: {i['name']} - Price: {i['price']} - code: {i['code']}")

    # input the code number of the item you want to get
    query = int(input("Enter the code number of the item you want to get: "))
    # Returns the list of items in the list.
    for i in items:
        if query == i["code"]:
            item = i
    # check if the item is empty
    if item == "":
        print("INVALID CODE")

    # function to perform cost of item
    else:
        print(f"Great, {item['name']} will cost you {item['price']} dollars")

        # function to perform the payment of the item
        # the change of the item if the payment is more than the price of the item
        price = int(input(f"Enter {item['price']} dollars to purchase: "))

        if price == item["price"]:
            # This function is called by the user when the user clicks on the buying button.
            print(f"Thank you for buying here is your {item['name']}")

        # This function is called when user enter a dollars
        else:
            print(f"Please enter only {item['price']} dollars")

    # This method is called by the user when the user clicks on the button.
    ## Generating docstring for this python vending machine finalization
    """
    --- It asks the user if they want to continue or quit the program.
    --- So to continue they can enter anything except q because that is for quitting.
    """

    query = input("To quit the machine enter q and to continue buying enter anything: ")
    # This is a shortcut for the method to set the query to c.
    is_quit = query != "c"
    print("")
