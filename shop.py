_input = input

def input(q):
    return _input(q + "\n")

class ShopException(Exception): # abstract class
    def __init__(self, message=""): # pass in the message when the exception is raised
        super().__init__(message)

class FundsError(ShopException):
    pass


class Shop:
    def __init__(self, shop_name):
        self.items = {}
        self.shop_name = shop_name
        self.user = None

    def add_user(self, name):
        self.user = name 
        self.balance = None
        
    def greet_user(self):
        print(f"Welcome {self.user.name}! This is the {self.shop_name}\nThe products available today are:")
        for key, values in self.items.items():
            print("-", key, ": £", values['price'], "( Stock:", values['stock'],")")

    def exit_option(self,response):
        if response == "n":
            print("You have entered the Computer Store.")
        elif response == "y":
            print("Exiting the shop...")
            exit()
        else:
            raise ValueError("Value must be 'y' or 'n'")

class User:
    def __init__(self, name, balance, shop):
        self.balance = balance 
        self.basket = []
        self.name = name
        self.shop = shop
        self.basketcost = 0
        self.attempts = 0

    def add_money(self,response):
        try:
            amount = round(float(response),2)
            self.balance += amount
            print(f"Your balance is now £ {self.balance}")
        except ValueError:
            print("Invalid input. Must be in numerical format with no special characters")

    def get_balance(self):
        print(f"Your balance is £ {self.balance}")

    def view_basket(self):
        if self.basket:
            print(f"Your basket currently contains {self.basket} and the total is £ {round(self.basketcost,2)}")
        else:
            print("Your basket is empty")

    def add_item(self,response):
        if response not in self.shop.items.keys():
            print(f"Invalid item, {response} could not be added to your basket") 
        elif self.shop.items[response]["stock"] == 0:
            print("Sorry this item is out of stock on the shelves")
        elif response in self.shop.items.keys() and (self.shop.items[response]["price"] <= (self.balance)):
            self.basket.append(response)
            self.basketcost += self.shop.items[response]["price"] #25
            self.balance -= self.shop.items[response]["price"] #75
            self.shop.items[response]["stock"] -= 1
            print(f"{response} has been added to your basket. You have £ {self.balance} left to spend if you make these purchases")

        else:
            if self.attempts < 2:
                self.attempts +=1 #balance 10, item 40 item - balance
                print(f"Item could not be added. Adding this item would make your basket £ {round(self.shop.items[response]['price'] - self.balance,2)} greater than your balance")
                print(f"To avoid being removed from the store, please do not attempt to make purchases with insufficient funds. You have {3-self.attempts} chances remaining.")
            else:
                raise FundsError("3 attempts of purchases with insufficient funds.")

    def remove_item(self):
        if self.basket:
            try:
                response = input("Which item do you want to remove?")
                self.basket.remove(response)
                self.balance += self.shop.items[response]["price"]
                self.shop.items[response]["stock"] += 1
                print(f"{response} has been removed! Your basket is now {self.basket}")
            except ValueError:
                print("Item is not in your basket. The item could not be removed.")
        else:
            print("No items to remove. Your basket is empty.")

    def view_shelves(self):
        for key, values in self.shop.items.items():
            print("-", key, ": £", values['price'], "( Stock:", values['stock'],")")

    def make_selection(self):
        response = input("Make a selection:\n- View basket\n- View shelves\n- Get balance\n- Add money\n- Add item\n- Remove item\n- Checkout\n- Leave shop").lower()
        if response == "leave shop":
            print("Thanks for shopping!")
            exit()
        elif response == "view basket":
            self.view_basket()
        elif response == "get balance":
            self.get_balance()
        elif response == "add money":
            money_wanted = input("How much money do you want to add e.g. 100?")
            self.add_money(money_wanted)
        elif response == "add item":
            item_wanted = input("Which item do you want to purchase?").lower()
            self.add_item(item_wanted)
        elif response == "checkout":
            self.checkout()
        elif response == "remove item":
            self.remove_item()
        elif response == "view shelves":
            self.view_shelves()
        else:
            print("Invalid response")

    def checkout(self):
        if self.basket:
            print("Thank you for shopping with Tech Store! Your purchases are:")
            for item in self.basket:
                print(item)
            exit()
        else:
            print("Your basket is empty. Either add to your basket or leave the shop.")

  
            



name = input("What is your name?")
if not name:
    print("You must enter a name. Run again.")
    exit()
comp_shop = Shop("Tech Store")
new_user = User(name, 100, comp_shop)
comp_shop.items = {"xbox": {"price" :400, "stock": 1}, "controller": {"price": 25, "stock": 5}, "disk drive": {"price":16.99, "stock": 2}, "mouse": {"price":15.50, "stock": 3}}

comp_shop.add_user(new_user)
comp_shop.greet_user()
inpt = input("Do you want to exit? Respond with y/n")
comp_shop.exit_option(inpt)


while True:
    new_user.make_selection()
