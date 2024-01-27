a1 = str(input(f"Enter Birth Month 1: "))
a2 = str(input(f"Enter Birth Month 2: "))
a3 = str(input(f"Enter Birth Month 3: "))
a4 = str(input(f"Enter Birth Month 4: "))
a5 = str(input(f"Enter Birth Month 5: "))
a6 = str(input(f"Enter Birth Month 6: "))

g1 = set([a1, a2, a3])
g2 = set([a4, a5, a6])

print(g1)
print(g2)

month = input("Enter your Birth Month: ")

print(f"Union: {str(g1|g2)}")
print(f"Intersection: {str(g1&g2)}")
print(f"Difference: {str(g1-g2)}")

if g1.issubset(month):
    print("You have the same birth month as one of your classmates")