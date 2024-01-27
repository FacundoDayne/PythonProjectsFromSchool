def movieQueue(counter):
    movies.append(input(f"Enter movie {str(counter)} of 3: "))
    if counter != 3:
        counter += 1
        movieQueue(counter)

def snackQueue(counter):
    snacks.append(input(f"Enter Snack {str(counter)} of 3: "))
    if counter != 3:
        counter += 1
        snackQueue(counter)
    
def snackTime():
    ans = str(input(f"Press S everytime you finish a snack "))
    if ans.capitalize() == "S":
        snacks.pop()
        if not snacks:
            print("No more snacks!")
        else:
            print(f"deque: {str(snacks)}")
            snackTime()

movies = []
snacks = []
movieQueue(1)
snackQueue(1)
print(f"Movies to watch are: deque {str(movies)}")
print(f"Snacks available are: deque {str(snacks)}")
snackTime()