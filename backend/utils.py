import yfinance as yf


def get_stock_info(ticker):

    company_data = yf.Ticker(ticker)

    company_data_cleaned = {
        i: (company_data.info[i] if i in company_data.info else None)
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

    # catch if the stock is not found
    if company_data_cleaned["longName"] == "longName":
        return False

    return company_data_cleaned
