# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({
    "FirstName": "Ben",
    "LastName": "Holland",
    "Residence": "San Diego",
    "Owns_Shoes":["Vans", "Timberland", "Converse"]
})

InfoDb.append({
    "FirstName": "Jayson",
    "LastName": "Borg",
    "Residence": "San Diego",
    "Owns_Shoes":["Timberland","Nike","Vans", "Converse"]
})

InfoDb.append({
    "FirstName": "Anthony",
    "LastName": "Pacheco",
    "Residence": "San Diego",
    "Owns_Shoes":["Vans","Nike"]
})

InfoDb.append({
    "FirstName": "Ben",
    "LastName": "Shamloufard",
    "Residence": "San Diego",
    "Owns_Shoes":["Vans","Nike","Puma"]
})

InfoDb.append({
    "FirstName": "Kian",
    "LastName": "Pasokhi",
    "Residence": "San Diego",
    "Owns_Shoes":["Converse","Reebok", "Nike", "Vans"]
})

InfoDb.append({
    "FirstName": "Daniel",
    "LastName": "Bertino",
    "Residence": "San Diego",
    "DOB": "March 14",
    "Age": "18",
    "Sports": ["Basketball","Soccer"],
    "Fav_Food": "Pizza",
    "School": "DNHS",
    "Subjects": ["cs","stats","literature","econ"],
    "Owns_Shoes":["Addidas","Puma","Vans"]
})

def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Shoes: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Shoes"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

# for loop iterates on length of InfoDb
def for_loop():
    print("=" * 25)
    print("For loop")
    print("-" * 25)
    for n in range(len(InfoDb)):
        print_data(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    print("=" * 25)
    print("While loop")
    print("-" * 25)
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def while_loop_run():
    while_loop(0)

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

def recursive_loop_run():
    print("=" * 25)
    print("Recursive loop")
    print("-" * 25)
    recursive_loop(0)
    print("=" * 25)

def list_finder():
    num = int(input("Which index do you want to search (0-" + str(len(InfoDb)-1) +"): "))
    print("-" * 25)
    try:
        # Prints all info of the given index
        print(InfoDb[num]["FirstName"] + " "+ InfoDb[num]["LastName"])
        print("Residence: " + InfoDb[num]["Residence"])
        print("Owns Shoes: ")
        for i in range (0, len(InfoDb[num]["Owns_Shoes"])):
            print("  - " + InfoDb[num]["Owns_Shoes"][i])
    except:
        # Prints this if the index is not in the list
        print("Invalid index given.")

def tester():

    for_loop()

    while_loop(0)  # requires initial index to start while

    recursive_loop_run(0)  # requires initial index to start recursion

    list_finder()

# this only applies if the file is run as main
if __name__ == "__main__":
    tester()