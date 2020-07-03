import requests
import dateutil.parser
from TopSecrets import *
from prettytable import PrettyTable
from colorama import Fore, Back, Style

class Three:

    def justDoIt(self):
        request = requests.get(TopSecrets.globalURL, headers=TopSecrets.requestHeaders)
        dataSet = request.json()["data"]

        table1 = PrettyTable()
        table1.title = "[Latest Global Market Metrics] [1/3]"
        table1.field_names = ["BTC_Dominance", "ETH_Dominance", "Active_Cryptocurrencies"]
        btc_dominance = Fore.GREEN + str(round(dataSet["btc_dominance"], 2)) + "%" + Style.RESET_ALL
        eth_dominance = Fore.GREEN + str(round(dataSet["eth_dominance"], 2)) + "%" + Style.RESET_ALL
        active_currencies = Fore.GREEN + str(dataSet["active_cryptocurrencies"]) + Style.RESET_ALL
        table1.add_row([btc_dominance, eth_dominance, active_currencies])

        table2 = PrettyTable()
        table2.title = "[Latest Global Market Metrics] [2/3]"
        table2.field_names = ["Total_Cryptocurrencies", "Active_Market_Pairs",
        "Active_Exchanges"]
        total_currencies = Fore.GREEN + str(dataSet["total_cryptocurrencies"]) + Style.RESET_ALL
        active_market_pairs = Fore.GREEN + str(dataSet["active_market_pairs"]) + Style.RESET_ALL
        active_exchanges = Fore.GREEN + str(dataSet["active_exchanges"]) + Style.RESET_ALL
        table2.add_row([total_currencies, active_market_pairs , active_exchanges])

        table3 = PrettyTable()
        table3.title = "[Latest Global Market Metrics] [3/3]"
        table3.field_names = ["Total_Exchanges", "Total_Market_cap",
        "Total_Volume_24h"]
        total_exchanges = Fore.GREEN + str(dataSet["total_exchanges"]) + Style.RESET_ALL
        total_market_cap = Fore.GREEN + "$" + "{:,}".format(round(dataSet["quote"]["USD"]["total_market_cap"])) + Style.RESET_ALL
        total_volume_24h = Fore.GREEN + "$" + "{:,}".format(round(dataSet["quote"]["USD"]["total_volume_24h"])) + Style.RESET_ALL
        table3.add_row([total_exchanges, total_market_cap, total_volume_24h])

        print()
        print(table1)
        print()
        print(table2)
        print()
        print(table3)
