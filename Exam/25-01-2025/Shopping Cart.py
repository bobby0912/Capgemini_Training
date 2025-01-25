items=[]
prices=[]
total_items=0

def add_item(item_name,price):
    items.append(item_name)
    prices.append(int(price))

def view_cart():
    # for i in items:
    #     print(i)
    print("Cart contains following items: ")
    for i in range(total_items):
        print(items[i],end=" ")
        print(prices[i])

def total_cart_value():
    return sum(prices)

while True:
    print("1. Add Items\n2. View cart Items.\n3. Calculate the total price\n4. Exit")
    option=int(input())
    if(option>4):
        print("Invalid Option")
        continue

    if(option==1):
        print("Enter item and price: ")
        item_name,price=input().split()
        add_item(item_name,price)
        total_items+=1

    elif(option==2):
        view_cart()
            # print(f"{{items[i]}   {prices[i]}}")
    
    elif(option==3):
        print(f"Total cart value: {total_cart_value()}")
    
    elif(option==4):
        break
    
    else:
        print("Invalid Option")
    print()
    