import json
import requests
from colorama import Fore, Style
from TopSecrets import *
from prettytable import PrettyTable

class KeyValidation:
    def validateTheKey(self):
        obj = TopSecrets()

        try:
            newKey = input(Fore.GREEN + "\nBefore the start, you have to write CoinMarketAPI key.\n" + Style.RESET_ALL)
        except:
            print("\nYou have to input some string value.\n")
            exit(0)

        obj.setKey(newKey)

        request = requests.get(obj.keyURL, headers=obj.requestHeaders)
        dataSet = request.json()["data"]
        left_credit_daily = dataSet["usage"]["current_day"]["credits_left"]
        total_credit_daily = dataSet["plan"]["credit_limit_daily"]
        percentage_of_daily_credit_count = round(left_credit_daily / total_credit_daily, 2)

        status_code_of_request = request.status_code

        """
        Furthermore information =>
        https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
        """

        if (status_code_of_request == 400):
            print("\nThe 400 Bad Request Error is an HTTP response status code that indicates that the server was unable to process the request sent by the client due to invalid syntax\n")
            exit(0)
        elif (status_code_of_request == 401):
            print("\nThe HTTP 401 Unauthorized client error status response code indicates that the request has not been applied because it lacks valid authentication credentials for the target resource.\n")
            exit(0)
        elif (status_code_of_request == 403):
            print("\nThe HTTP 403 Forbidden client error status response code indicates that the server understood the request but refuses to authorize it.\n")
            exit(0)
        elif (status_code_of_request == 429):
            print("\nThe HTTP 429 Too Many Requests response status code indicates the user has sent too many requests in a given amount of time ('rate limiting').\n")
            exit(0)
        elif (status_code_of_request == 500):
            print("\nThe HyperText Transfer Protocol (HTTP) 500 Internal Server Error server error response code indicates that the server encountered an unexpected condition that prevented it from fulfilling the request.\n")
            exit(0)

        print(Fore.GREEN + "\nYou successfully logged into CoinMarketCap API database." + Style.RESET_ALL + "\n")
        print("Left Daily Credit Count: " +  Fore.GREEN + "[" +  str(left_credit_daily) +  "/" + str(total_credit_daily) + "] ≈ %" + str(percentage_of_daily_credit_count) + Style.RESET_ALL)
        print("Used Daily Credit Count: " + Fore.RED + "[" + str(total_credit_daily - left_credit_daily) + "/" + str(total_credit_daily) + "] ≈ %" + str(1.00 - percentage_of_daily_credit_count) + Style.RESET_ALL)
        print("Your daily credit count will be refresh in: " + Fore.GREEN + dataSet["plan"]["credit_limit_daily_reset"] + Style.RESET_ALL + "\n")