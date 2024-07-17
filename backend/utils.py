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

    # calculating EV/EBITDA
    # print(company_data.cashflow/company_data.info['marketCap'])
    market_cap = company_data.info["marketCap"]

    # Fetch balance sheet to get total debt and cash
    balance_sheet = company_data.balance_sheet
    total_debt = balance_sheet.loc["Total Debt"][0]
    cash_and_equivalents = balance_sheet.loc["Cash And Cash Equivalents"][0]

    # Calculate Enterprise Value (EV)
    enterprise_value = market_cap + total_debt - cash_and_equivalents

    # Fetch income statement to get EBITDA
    income_statement = company_data.financials
    ebitda = income_statement.loc["EBITDA"][0]

    # Calculate EV/EBITDA ratio
    ev_to_ebitda = enterprise_value / ebitda

    company_data_cleaned["free cash flow yield"] = (
        company_data.info["freeCashflow"] / company_data.info["marketCap"]
    )

    company_data_cleaned["evToEbitda"] = ev_to_ebitda

    return company_data_cleaned
