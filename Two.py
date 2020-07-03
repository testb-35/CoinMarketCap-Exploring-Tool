import json
import locale
import requests
from colorama import Fore, Style
from TopSecrets import *
from prettytable import PrettyTable

class Two:
    def justDoIt(self):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

        globalRequest = requests.get(TopSecrets.globalURL, headers=TopSecrets.requestHeaders)
        dataSet = globalRequest.json()["data"]
        total_market_cap = dataSet["quote"]["USD"]["total_market_cap"]

        try:
            limit = int(input(Fore.GREEN + "\nWrite the limit of the data count: \n" + Style.RESET_ALL))
        except:
            print("\nYou have to input some valid integer value!\n")
            exit(0)

        requestParameters = {
            "limit" : limit
        }

        listingRequest = requests.get(TopSecrets.listingURL, params=requestParameters, headers=TopSecrets.requestHeaders)
        dataSet = listingRequest.json()["data"]

        table1 = PrettyTable()
        table1.title = "[Future Value of Top Cryptocurrencies] [1/2]"
        table1.field_names = ["Name", "% of total market cap", "Current",
        "10.9T (Gold)", "35.2T (Narrow Money)"]

        table2 = PrettyTable()
        table2.title = "[Future Value of Top Cryptocurrencies] [2/2]"
        table2.field_names = ["89.5T (Total Stock Markets)", "95.7T (Broad Money)",
        "280.6T (Real Estate)", "558.5T (Derivatives)"]

        for data in dataSet:
            name = data["name"]
            symbol = data["symbol"]
            percentage_of_total_market_cap = data["quote"]["USD"]["market_cap"] / total_market_cap
            price = round(data["quote"]["USD"]["price"], 2)

            percentage_of_total_market_cap_string = str(round(percentage_of_total_market_cap * 100, 2)) + "%"
            price = str(price) + "$"

            total_supply = data["total_supply"]

            gold = round(10900000000000 * percentage_of_total_market_cap / total_supply, 2)
            narrow_money = round(35200000000000 * percentage_of_total_market_cap / total_supply, 2)
            total_stock_markets = round(89500000000000 * percentage_of_total_market_cap / total_supply, 2)
            broad_money = round(95700000000000  * percentage_of_total_market_cap / total_supply, 2)
            real_estate = round(280600000000000  * percentage_of_total_market_cap / total_supply, 2)
            derivatives = round(558500000000000 * percentage_of_total_market_cap / total_supply, 2)

            gold = "$" + locale.format("%.2f", gold, True)
            narrow_money = "$" + locale.format("%.2f", narrow_money, True)
            total_stock_markets = "$" + locale.format("%.2f", total_stock_markets, True)
            broad_money = "$" + locale.format("%.2f", broad_money, True)
            real_estate = "$" + locale.format("%.2f", real_estate, True)
            derivatives = "$" + locale.format("%.2f", derivatives, True)

            row1 = [name, percentage_of_total_market_cap_string, price, gold, narrow_money]
            row2 = [total_stock_markets, broad_money, real_estate, derivatives]

            table1.add_row(row1)
            table2.add_row(row2)

        print()
        print(table1)
        print()
        print(table2)
        print()