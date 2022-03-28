import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame

API_KEY = ""
API_SECRET = ""
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"


class SampleTrade:

    def __init__(self):
        self.alpaca = tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL,
                                    'v2')

        stockUniverse = [
            'AAPL',
        ]
        # Format the allStocks variable for use in the class.
        self.allStocks = []
        for stock in stockUniverse:
            self.allStocks.append([stock, 0])

        self.long = []
        self.short = []
        self.qShort = None
        self.qLong = None
        self.adjustedQLong = None
        self.adjustedQShort = None
        self.blacklist = set()
        self.longAmount = 0
        self.shortAmount = 0
        self.timeToClose = None

    def load_bars(self):
        bars = self.alpaca.get_bars("AAPL",
                                    TimeFrame.Hour,
                                    "2021-06-08",
                                    "2021-06-08",
                                    adjustment='raw').df
        print(bars)

    def load_trades(self):
        trades = self.alpaca.get_trades("AAPL",
                                        "2021-06-08",
                                        "2021-06-08",
                                        limit=10).df
        print(trades)

    def load_quotes(self):
        quotes = self.alpaca.get_quotes("AAPL",
                                        "2021-06-08",
                                        "2021-06-08",
                                        limit=10).df
        print(quotes)


# Run the SampleTrade class
st = SampleTrade()
st.load_bars()
st.load_trades()
st.load_quotes()