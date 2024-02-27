Rutine = ["bathing", "eating", "reading", "sleeping"]

_check_rutine = int(input("Kindly enter your first rutine here (1-4): "))

if _check_rutine == 1:
    print("You have to eat now")
elif _check_rutine == 2:
    print("Go on with your rutine")
else:
   print("Please check your rutine input")
    
    
import os

Rutine = ["bathing", "eating", "reading", "sleeping"]

# Prompt the user for input
_check_rutine = os.sys.stdin.readline().strip()
_check_rutine = int(_check_rutine)

if _check_rutine == 1:
    print("You have to eat now")
elif _check_rutine == 2:
    print("Go on with your rutine")
else:
    print("Please check your rutine input")
    print("You are welcome")

    