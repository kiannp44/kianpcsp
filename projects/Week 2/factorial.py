# Hack 2: Write Factorial function using classes, providing implementation of call.
# Print final number

# to run: type "python week2/factorial.py" (without quotes) in the shell

class Factorial:
    def __init__(self):
        self.factoSeq = [1, 1]
    def __call__(self, n):
        if n < len(self.factoSeq):
            return self.factoSeq[n]
        else:
            # Compute the requested Factorial number
            facto_number = n * self(n - 1)
            # two recursive calls to self (__call__(self, n))
            self.factoSeq.append(facto_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.factoSeq[n]

def printfac():
    facto_of = Factorial() # object instantiation and run __init__ method

    print("The Factorial of 10 is: ")
    print(facto_of(10))

    print("The Factorial of 14 is: ")
    print(facto_of(14))

if __name__ == "__main__":
    printfac()