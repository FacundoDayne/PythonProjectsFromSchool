# Function to get student name from number
def get_name_from_number(num):
    return StuNo.get(num, "Number not found")

# Function to get student number from name
def get_number_from_name(name):
    for num, student_name in StuNo.items():
        if student_name == name:
            return num
    return "Name not found"

# Dictionary
StuNo = {}

a1 = str(input("Enter Student 1's Student Number: "))
a2 = str(input("Enter Student 1's First Name: "))
a3 = str(input("Enter Student 2's Student Number: "))
a4 = str(input("Enter Student 2's First Name: "))
a5 = str(input("Enter Student 3's Student Number: "))
a6 = str(input("Enter Student 3's First Name: "))

# Assigns the values to the dictionary
# a1, a3, and a5 are the Keys
# a2, a4, and a6 are the Values
StuNo = {a1 : a2, a3 : a4, a5 : a6}
print("Student List")
for x,y in StuNo.items():
    print (x, y)

del StuNo[a5]
a1 = str(input("Enter your Student Number: "))
a2 = str(input("Enter your First Name: "))
StuNo[a1] = a2
print("Student List")
for x,y in StuNo.items():
    print (x, y)


while True:
    choice = input("Enter 'N' to get name from number, 'S' to get number from name, or 'Q' to quit: ")
    if choice.upper() == 'N':
        num = input("Enter student number: ")
        print(get_name_from_number(num))
    elif choice.upper() == 'S':
        name = input("Enter student name: ")
        print(get_number_from_name(name))
    elif choice.upper() == 'Q':
        break
    else:
        print("Invalid choice. Please enter 'N', 'S', or 'Q'.")