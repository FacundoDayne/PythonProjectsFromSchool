def catcher (counter, i):
    fruit = str(input("Fruit " + str(i) + " of " + str(counter) + " : "))
    if fruit.capitalize() == "A":
        basket.append("Apple")
    elif fruit.capitalize() == "O":
        basket.append("Orange")
    elif fruit.capitalize() == "M":
        basket.append("Mango")
    elif fruit.capitalize() == "G":
        basket.append("Guava")
    else:
        i -= 1
        print("Please press A, O, M, or G.")
    if counter != i:
        i += 1
        catcher (counter, i)

def showBasket():
    print ("Your basket now has: " + str(basket))
    eat = str(input("Press E to eat a fruit. "))
    if eat.capitalize() == "E":
        basket.pop()
    if not basket:
        print ("Your basket is empty!")
    else:
        showBasket()

print("Catch and eat one of these fruits:('apple', 'orange', 'mango', 'guava')")
counter = int(input("How many fruits would you like to catch? "))
print("Choose a fruit to catch. Press A, O, M, or G. ")
basket = []
catcher(counter, 1)
showBasket()