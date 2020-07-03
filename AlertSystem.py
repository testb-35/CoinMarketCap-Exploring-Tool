import json
import requests
import os
import pytz
import time
import dateutil
from colorama import Fore, Style
from datetime import datetime
from TopSecrets import *

class AlertSystem:
    def justDoIt(self):
        print("\n[Cryptocurrency Alert] started to tracking!\n")
        name = input(Fore.GREEN + "Write the name of cryptocurrency name: " + Style.RESET_ALL)
        expected = float(input(Fore.GREEN + "Write the expected price: " + Style.RESET_ALL))
        print()

        request = requests.get(TopSecrets.listingURL, headers=TopSecrets.requestHeaders)
        dataSet = request.json()["data"]

        isSpecifiedDataFound = False

        for data in dataSet:
            if (data["name"] == name):
                isSpecifiedDataFound = True
                break

        if (isSpecifiedDataFound):
            isHit = False

            while (isHit == False):
                specifiedData = {}

                try:
                    request = requests.get(TopSecrets.listingURL, headers=TopSecrets.requestHeaders)
                except:
                    os.system("say Sir, I can not establish the connection.")
                    os.system("say Please, re-start the system again!")
                    exit(0)

                jsonOutput = request.json()

                for data in jsonOutput["data"]:
                    if (data["name"] == name):
                        specifiedData["price"] = data["quote"]["USD"]["price"]
                        gmt_3 = pytz.timezone("Europe/Istanbul")
                        lastUpdated = dateutil.parser.parse(data["last_updated"]).astimezone(gmt_3)
                        specifiedData["lastUpdated"] = lastUpdated.strftime("%m/%d/%Y, %H:%M:%S")
                        break

                price = specifiedData["price"]

                if (expected >= price):
                    os.system("say Sir, price is currently as you wish!")
                    os.system("say I am going to send the details now.")
                    os.system("say Have a good day sir!")
                    print("\nCurrent Price: $" + str(price) + ", $" +
                    str(abs(round(expected-price, 2))) + " lower than $" +
                    str(expected) + "\n")
                    print("Cryptocurrency updated on " + specifiedData["lastUpdated"] + "\n")
                    isHit = True
                else:
                    try:
                        doesContinue = input("Do you want to continue? (y/n): ")
                    except:
                        print("\n You have to input some string value. (y/n): ")
                        exit(0)

                    if (doesContinue != "y" and doesContinue != "n"):
                        print("\n You have to write (y/n).")
                        exit(0)

                    if (doesContinue):
                        os.system("say Sir, I am not able to find the price as you wish.")
                        os.system("say I will start the next search in 1 minutes.")
                        os.system("say After 1 minutes, I will notify you. Enjoy!")
                        print("Current Price: $" + str(price) + ", $" +
                        str(abs(round(price-expected, 2))) + " greater than $" +
                        str(expected) + "\n")
                        time.sleep(60)
                    else:
                        exit(0)
        else:
            print(Fore.RED + "\nSpecified cryptocurrency name is not found in CoinMarketCap database." + Style.RESET_ALL)