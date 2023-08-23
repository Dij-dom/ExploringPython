'''Lala Ghansham Ji is the local vendor of your locality who is running a grocery shop. He wants your help to
digitize his day to day transactions and monthly business. Find out whether he is making profit or loss on a daily
basis and what is his monthly income from the grocery shop? Can you help him out in doing so? You are free
to imagine your own real time set up for grocery shop and create user-defined functions to accomplish the task.'''

# Function to accept item details from the vendor, saved to items_data dictionary
def accept_items_data():
    items_data = {}
    num_items = int(input("Enter the number of items sold in the shop: "))

    for i in range(num_items):
        item_name = input(f"Enter the name of item {i+1}: ")
        buying_price = float(input(f"Enter the buying price of {item_name}: "))
        selling_price = float(input(f"Enter the selling price of {item_name}: "))
        items_data[item_name] = {"buying_price": buying_price, "selling_price": selling_price}

    return items_data

# Function to accept daily transactions from the vendor
def accept_daily_transactions():
    transactions = []
    
    num_days = int(input("Enter the number of days for which you want to enter transactions: "))

    for day in range(num_days):
        sales = {} #contains sold itemname as key and the quantity of the item as value
        purchases = {} #contains purchased itemname as key and the quantity of the item as value

        num_sales = int(input(f"Enter the number of different items sold on day {day+1}: "))
        for i in range(num_sales):
            while True:
                item_name = input(f"Specify the item sold: ")
                if item_name not in items_data:
                    print("Enter a valid item.")
                else:
                    break
            quantity = int(input(f"Enter the quantity (in kgs) of {item_name} sold: "))
            sales[item_name] = quantity

        num_purchases = int(input(f"Enter the number of items purchased on day {day+1}: "))
        for i in range(num_purchases):
            
            while True:
                item_name = input(f"Specify the item purchased: ")
                if item_name not in items_data:
                    print("Enter a valid item.")
                else:
                    break
            quantity = int(input(f"Enter the quantity (in kgs) of {item_name} purchased: "))
            purchases[item_name] = quantity

        transactions.append({"sales": sales, "purchases": purchases})
    return transactions


# Function to calculate daily profit/loss
def calculate_daily_profit_loss(sales, purchases, items_data):
    daily_profit = 0
    for item, quantity in sales.items():
        if item in items_data:
            item_data = items_data[item]
            selling_price = item_data["selling_price"]
            buying_price = item_data["buying_price"]
            # print("Selling price is ", selling_price)
            # print("Buying price is ", buying_price)
            daily_profit += (selling_price - buying_price) * quantity
    return daily_profit

# Function to calculate monthly income
def calculate_monthly_income(transactions, items_data):
    monthly_income = 0
    for day_transactions in transactions:
        daily_profit = calculate_daily_profit_loss(day_transactions["sales"], day_transactions["purchases"], items_data)
        monthly_income += daily_profit
    return monthly_income


print()
print("Welcome to Personalized Shop Manager.\n")
items_data = accept_items_data()    # Accept items data from the vendor
transactions = accept_daily_transactions()  # Accept daily transactions from the vendor


for day, daily_transactions in enumerate(transactions, start=1):            # Calculate daily profit/loss for each day and monthly income
    daily_profit = calculate_daily_profit_loss(daily_transactions["sales"], daily_transactions["purchases"], items_data)
    print(f"Day {day} - Profit/Loss: {daily_profit}")


monthly_income = calculate_monthly_income(transactions, items_data)
print(f"Monthly Income: {monthly_income}")
if daily_profit <0:
    print("It's a loss!, Foucs on your business more.")
elif daily_profit == 0:
    print("Try to make profit")
else:
    print("You are rocking in your business. Go ahead.")
