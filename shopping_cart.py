#shopping cart 

foods = []
prices = []
total = 0 

while True:
    food = input("enter your order: ")
    if(food.lower() == "q"):
        break
    else:
        price = int(input("enter price: "))
        foods.append(food)
        prices.append(price) 

print("---------- YOUR CART ----------")
for food in foods:
    print(food, end = " ")
print()
for price in prices:
    total += price 

print(f"Your total price is : {total}")
