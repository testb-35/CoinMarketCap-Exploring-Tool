from ListTheCryptocurrencies import *
from ListTheFutureValuesOfCryptocurrencies import *
from ListTheGlobalMarketMetrics import *
from AlertSystem import *
from StoreDataIntoExcel import *
from KeyValidation import *

def printIntro():
    print("\n\t[CoinMarketCap Exploring Tool] using CoinMarketCap API\n\t")
    print("1 - Show the Top (X) sorted by (Y).")
    print("2 - Show the potential Top (X)'s portfolio.")
    print("3 - Show the latest global cryptocurrency market metrics.")
    print("4 - Start the alert.")
    print("5 - Store the currencies into Excel file.")
    print("0 - Exit.\n")

printIntro()

keyObj = KeyValidation()
obj1 = ListTheCryptocurrencies()
obj2 = ListTheFutureValuesOfCryptocurrencies()
obj3 = ListTheGlobalMarketMetrics()
obj4 = AlertSystem()
obj5 = StoreDataIntoExcel()

keyObj.validateTheKey()
print()

while (True):
    try:
        number = int(input(Fore.GREEN + "What is your choice? [0,5]: " + Style.RESET_ALL))
    except:
        print("\nYou have to input some integer value to choose.\n")
        exit(0)

    if (number == 0):
        exit(0)
    if (number == 1):
        obj1.justDoIt()
    elif (number == 2):
        obj2.justDoIt()
    elif (number == 3):
        obj3.justDoIt()
    elif (number == 4):
        obj4.justDoIt()
    elif (number == 5):
        obj5.justDoIt()
    else:
        print("\nYou have to input some valid integer value. [0,5]\n")
        exit(0)

    try:
        response = input("\nDo you want to continue? (y/n)\n")
    except:
        print("\nYou have to input some string value.\n")
        exit(0)

    if (response != "n" and response != "y"):
        print("\nYou have to input 'yes' or 'no'.\n")
        exit(0)
    elif (response == "n"):
        exit(0)

    printIntro()


