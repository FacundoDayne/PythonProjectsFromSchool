num = 0

def find_Sum(a):
    if a != 0:
        global num
        num += a
        return find_Sum(a-1)
    else:
        return num
    
ans = int(input("Please enter a number"))
print(f"The sum of the first {ans} numbers is {find_Sum(ans)}")
