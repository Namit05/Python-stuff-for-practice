# CONCESSION STAND PROGRAM

menu={"Pizza":3.50,
      "Popcorn":4.00,
      "Burger":3.50,
      "Popscicle" :5.00}

cart=[]
total=0
print("------MENU------")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------")

while True:
    food=input("Select an item (q to quit) : ").lower()
    if food == "q":
        break

    elif menu.get(food) is not None :
        cart.append(food)


for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()

print(f"Total is: ${total:.2f}")
