from TopSecrets import *
from colorama import Fore, Style
import xlsxwriter
import os
import requests

class StoreDataIntoExcel:
    def justDoIt(self):
        try:
            limit = int(input(Fore.GREEN + "\nWrite the limit of the data count: " + Style.RESET_ALL))
        except:
            print("\nYou have to input some integer value.\n")
            exit(0)

        requestParameters = {
            "limit" : limit
        }

        request = requests.get(TopSecrets.listingURL, params=requestParameters, headers=TopSecrets.requestHeaders)
        dataSet = request.json()["data"]

        isHere = os.path.isfile('./cryptocurrencies.xlsx')

        if (isHere == False):
            f = open("cryptocurrencies.xlsx","w+")
            f.close()
            print(Fore.GREEN + "\nProgram created the 'cryptocurrencies.xlsx' file.\n" + Style.RESET_ALL)

        workbook = xlsxwriter.Workbook("cryptocurrencies.xlsx")
        sheet = workbook.add_worksheet()
        sheet.write("A1", "Rank")
        sheet.write("B1", "Name")
        sheet.write("C1", "Symbol")
        sheet.write("D1", "Market Cap")
        sheet.write("E1", "Volume (24h)")
        sheet.write("F1", "Circulating Supply")
        sheet.write("G1", "Change (24h)")

        for i in range(len(dataSet)):
            data = dataSet[i]
            rank = data["cmc_rank"]
            name = data["name"]
            symbol = data["symbol"]
            market_cap = "$"  + "{:,}".format(round(data["quote"]["USD"]["market_cap"]))
            volume_24 = "$" + "{:,}".format(round(data["quote"]["USD"]["volume_24h"]))
            circulating_supply = "{:,}".format(round(data["circulating_supply"]))
            change_24h = "{:,}".format(round(data["quote"]["USD"]["percent_change_24h"], 2))

            sheet.write(i + 1, 0, rank)
            sheet.write(i + 1, 1, name)
            sheet.write(i + 1, 2, symbol)
            sheet.write(i + 1, 3, market_cap)
            sheet.write(i + 1, 4, volume_24)
            sheet.write(i + 1, 5, circulating_supply)
            sheet.write(i + 1, 6, change_24h)

        workbook.close()

        print(Fore.GREEN + "All information was written into excel file." + Style.RESET_ALL)