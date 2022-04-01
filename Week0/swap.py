def swap(age1, age2):
    if (int(age1) > int(age2)):
        # swapping age by assigning one of them to a temp variable
        temp = age1
        age1 = age2
        age2 = temp
    return(age1, age2)

def swap_run():
    age1 = input("What is the first age? - ")
    age2 = input("What is the second age? - ")
    print("=" * 25)
    print("Original: ", age1, age2)
    age1, age2 = swap(age1, age2)
    print("Final: ", age1, age2)
    print("=" * 25)

# this only applies if the file is run as main
if __name__ == "__main__":
    swap_run()