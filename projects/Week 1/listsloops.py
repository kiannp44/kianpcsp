InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Kian",
    "LastName": "Pasokhi",
    "DOB": "October 29",
    "Residence": "San Diego",
    "Email": "kianpasokhi@gmail.com",
    "Owns_Shoes":["reebok", "converse", "nike", "new balance"]
})

InfoDb.append({
    "FirstName": "Morad",
    "LastName": "Pasokhi",
    "DOB": "June 19",
    "Residence": "San Diego",
    "Email": "moradpasokhi@gmail.com",
    "Owns_Shoes":["nike","puma","timberland", "skechers"]
})

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Shoes: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Shoes"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()

# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

## hack 2b: def while_loop(0)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

## hack 2c : def recursive_loop(0)

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion


if __name__ == "__main__":
    tester()
