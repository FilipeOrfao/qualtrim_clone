import yfinance as yf


def get_stock_info(ticker):
    stock_info = yf.Ticker(ticker)
    stock_info_wanted = {
        i: (stock_info.info[i] if i in stock_info.info else i)
        for i in [
            "marketCap",
            "shortName",
            "longName",
            "trailingPE",
            "forwardPE",
            "priceToSalesTrailing12Months",
            "evToEbitda",
            "priceToBook",
            "free cash flow yield",
            "freeCashflow",
            "poitroski score",
            "quality rating",
            "profitMargins",
            "operatingMargins",
            "quarterly earnings",
            "quarterly revenue",
            "totalCash",
            "totalDebt",
            "netIncomeToCommon",
            "dividendYield",
            "payoutRatio",
            "exDividendDate",
            "payout date",
        ]
    }

    return stock_info_wanted
