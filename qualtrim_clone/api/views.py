from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import datetime

# import matplotlib.pyplot as plt
import yfinance as yf


# Create your views here.
def health_check(request):
    return JsonResponse({"health": "ok"})


def dollar_cost_average(request, ticker):
    start_date = "2017-01-01"
    end_date = "2024-01-01"
    end_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(
        "%Y-%m-%d"
    )
    interval = "3M"
    ammount = 500

    data = yf.download(ticker, start=start_date, end=end_date)
    data = data.dropna()

    resampled_data = data.resample(interval).first()

    total_investement = 0
    total_shares = 0

    dca_log = []
    for date, row in resampled_data.iterrows():
        price = row["Adj Close"]

        total_shares += ammount / price
        total_investement += ammount

        dca_log.append(
            {
                "Date": date,
                "Price": price,
                "Total Shares": total_shares,
                "Total Investment": total_investement,
                "Portfolio Value": total_shares * price,
            }
        )
    # dca_log = pd.DataFrame(dca_log)
    # print(dca_log)

    return JsonResponse({"ticker": ticker, "data": dca_log})
