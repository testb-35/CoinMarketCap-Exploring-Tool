import json
import os
import pytz
import time
import requests
import dateutil.parser
from TopSecrets import *
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

class One:
    def justDoIt(self):
        try:
            sorting = input("\nChoose the sorting variable like market_cap: ")
            limit = int(input("\nChoose the limit of the data count: "))
        except:
            print("\nYou have to input some valid values.\n")
            exit(0)

        requestParameters = {
            "limit" : limit,
            "sort" : sorting
        }

        request = requests.get(TopSecrets.listingURL, params=requestParameters, headers=TopSecrets.requestHeaders)

        try:
            dataSet= request.json()["data"]
        except:
            print(Fore.RED + "\nSomething went wrong!\n" + Style.RESET_ALL)
            print(Fore.RED + "For more information: \n" +
            "https://coinmarketcap.com/api/documentation/" +
            "v1/#operation/getV1CryptocurrencyListingsLatest\n" + Style.RESET_ALL)
            exit(0)

        table = PrettyTable()
        table.title = "[Latest Listing of Active Cryptocurrencies]"
        table.field_names = ["Rank", "Name", "Market Cap", "Price",
        "Volume (24h)", "Circulating Supply", "Change (24h)"]

        for data in dataSet:
            rank = data["cmc_rank"]
            name = data["name"]
            marketCap = data["quote"]["USD"]["market_cap"]
            price = data["quote"]["USD"]["price"]
            volume24h = data["quote"]["USD"]["volume_24h"]
            circulatingSupply = data["circulating_supply"]
            change24h = data["quote"]["USD"]["percent_change_24h"]

            if (marketCap is None):
                marketCap = "NaN"
            else:
                marketCap = "$" + "{:,}".format(round(marketCap))

            if (price is not None):
                if (round(price) == 0):
                    price = round(price, 6)
                else:
                    price = round(price)

                price = "$" + "{:,}".format(price)
            else:
                price = "NaN"

            if (volume24h is None):
                volume24h = "NaN"
            else:
                volume24h = round(volume24h)
                volume24h = "$" + "{:,}".format(volume24h)

            if (circulatingSupply is None):
                circulatingSupply = "NaN"
            else:
                circulatingSupply = "{:,}".format(round(circulatingSupply))

            if (change24h is None):
                change24h = "NaN"
            else:
                change24h = round(change24h, 2)

            if (change24h > 0):
                change24h = Back.GREEN + str(change24h) + "%" + Style.RESET_ALL
            elif (change24h < 0):
                change24h = Back.RED + str(change24h) + "%" + Style.RESET_ALL
            else:
                change24h = Back.WHITE + str(change24h) + "%" + Style.RESET_ALL

            results = [rank, name, marketCap, price,
             volume24h, circulatingSupply, change24h]
            table.add_row(results)

        print(table)