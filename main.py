# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
# import patterns
# import stringy
# import listy
# import loopy
# import mathpy
# from mody import advy
# # abstracted files in a folder (aka module)
# from mody import questy
# from wipy import funcy
# from wipy import prefuncy
# Week 0 Imports
from Week0 import swap, matrix, anime
import os
# Week 1 imports
from Week1 import fibonacci, Listsloops
# Week 2 imports
from Week2 import mathfunction, palindrome, factorial, math

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
]

visual_sub_menu = [
    ["Animation", anime.animefunc],
    ["Matrix", matrix.matrix_tester],
]

math_sub_menu = [
    ["Swap", swap.swap_run],
    ["Fibonacci", mathfunction.fibonacci_tester],
    ["Recursive Fibonacci", mathfunction.recur_fibonacci_tester],
    ["Recursive Factorial", mathfunction.factorial_tester],
    ["Least Common Multiple", factorial.lcm_run]
]

oop_sub_menu = [
    ["OOP Fibonacci", math.fib_run],
    ["OOP Factorial", math.factorial_run],
    ["OOP Least Common Multiple", math.lcm_run],
    ['\u001b[32;1m[EXTRA CREDIT]\u001b[37;1m OOP Palindrome', palindrome.pali_tester],
]

data_sub_menu = [
    ["For Loop", Listsloops.for_loop],
    ["While Loop", Listsloops.while_loop_run],
    ["Recursive Loop", Listsloops.recursive_loop_run],
    ["List Search", Listsloops.list_finder],
]

# Menu banner and formatted borders
thinborder = "-" * 25
border = "=" * 25
banner = f"\n{thinborder}\nPlease Select An Option\n{border}"


def menu():
    title = f"{border}\n" + "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Visual", visual_submenu])
    menu_list.append(["Imperative Math", math_submenu])
    menu_list.append(["OOP Math", oop_submenu])
    menu_list.append(["Data", data_submenu])
    buildMenu(title, menu_list)

def visual_submenu():
    title = f"{border}\n" + "Patterns Submenu" + banner
    buildMenu(title, visual_sub_menu)

def math_submenu():
    title = f"{border}\n" + "Math Submenu" + banner
    # math_menu = math_sub_menu.copy()
    # math_menu.append(["OOP Submenu", oop_submenu])
    buildMenu(title, math_sub_menu)

def data_submenu():
    title = f"{border}\n" + "Data Submenu" + banner
    buildMenu(title, data_sub_menu)

def oop_submenu():
    title = f"{border}\n" + "OOP Function Submenu" + banner
    buildMenu(title, oop_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '-', value[0])

    # get user choice
    choice = input("Type your choice - ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            os.system("clear")
            return
        try:
            # try as function
            os.system("clear")
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # NAN error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # All other errors covered here
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()