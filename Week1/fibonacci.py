# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input

# Python program to display the Fibonacci sequence

# type "python week1/fibonacci.py" (without quotes) in the shell

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

def fibo_seq():
    print("Fibonacci sequence:")
    for i in range(terms):
        print(fibonacci(i))

def try_again():
    retry = int(input("How many terms? "))
    print("Fibonacci sequence:")
    for i in range(retry):
        print(fibonacci(i))


def fibo_print():
    try:
        terms = int(input("How many terms? "))
        assert terms > 0
    except ValueError:
        print("That's not a number")
        try_again()
    except AssertionError:
        print("You can't have a negative amount of terms smh")
        try_again()
    else:
        fibo_seq()

if __name__ == "__main__":
    fibo_print()