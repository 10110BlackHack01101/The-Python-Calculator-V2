#Calculator
import time
import sys
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
def rem_lst_lne():
    sys.stdout.write('\x1b[1A')

    sys.stdout.write('\x1b[2K')

def calcu():
    operator = input("What operation will you want: (* / + -) ")
    rem_lst_lne()
    first = input("First: ")
    rem_lst_lne()
    if first == "":
        print(color.RED + "Error " + color.BOLD +  "001" + color.END + ": Please rerun the program")    
    elif first == " ":
        print(color.RED + "Error " + color.BOLD +  "001" + color.END + ": Please rerun the program")
    else:
        second = input("Second: ")
        rem_lst_lne()
        if second == "":
            print(color.RED + "Error " + color.BOLD +  "002" + color.END + ": Please rerun the program")
        elif second == " ":
            print(color.RED + "Error " + color.BOLD +  "002" + color.END + ": Please rerun the program")
        else:
            if operator == "*":
                answer = float(first) * float(second)
                print("Calculating.")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating..")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating...")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating.")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating..")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating...")
                rem_lst_lne()
                time.sleep(1)
                print("The answer to " + color.BOLD + str(first) + operator +  str(second) + color.END + " is " + str(answer))
            elif operator == "/":
                answer = float(first) / float(second)
                print("Calculating.")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating..")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating...")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating.")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating..")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating...")
                rem_lst_lne()
                time.sleep(1)
                print("The answer to " + color.BOLD + str(first) + operator +  str(second) + color.END + " is " + str(answer))
            elif operator == "+":
                answer = float(first) + float(second)
                print("Calculating.")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating..")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating...")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating.")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating..")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating...")
                rem_lst_lne()
                time.sleep(1)
                print("The answer to " + color.BOLD + str(first) + operator +  str(second) + color.END + " is " + str(answer))
            elif operator == "-":
                answer = float(first) - float(second)
                print("Calculating.")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating..")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating...")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating.")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating..")
                rem_lst_lne()
                time.sleep(1)
                print("Calculating...")
                rem_lst_lne()
                time.sleep(1)
                print("The answer to " + color.BOLD + str(first) + operator +  str(second) + color.END + " is " + str(answer))
                time.sleep(5)
            else:
                print(color.RED + "Error " + color.BOLD + "003" + color.END + ": Please rerun the program")
rem_lst_lne()
input("Welcome to \"The Python-Calculator\"")
rem_lst_lne()
print("Loading")
time.sleep(2)
rem_lst_lne()
calcu()