class TopSecrets:
    listingURL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    globalURL = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest"
    keyURL = "https://pro-api.coinmarketcap.com/v1/key/info"

    requestHeaders = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': ""
    }

    def setKey(self, newKey):
        self.requestHeaders['X-CMC_PRO_API_KEY'] = newKey

    def getKey(self):
        return self.requestHeaders['X-CMC_PRO_API_KEY']