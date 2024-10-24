from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import datetime
import json

# import matplotlib.pyplot as plt
import yfinance as yf


# Create your views here.
def health_check(request):
    return JsonResponse({"health": "ok"})


def home(request):
    return render(request, "api/base.html", {"hello": "this is a greating"})


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

    # add a try here because sometime it can not reach the yfinance and the dataframe is empty
    resampled_data = data.resample(interval).last()

    total_investement = 0
    total_shares = 0

    dca_log = []
    for date, row in resampled_data.iterrows():
        price = row["Adj Close"]

        total_shares += ammount / price
        total_investement += ammount

        dca_log.append(
            {
                "date": date,
                "price": price,
                "total_shares": total_shares,
                "total_investment": total_investement,
                "portfolio_value": total_shares * price,
            }
        )

    dca_log = pd.DataFrame(dca_log)
    dca_log = dca_log.to_dict("records")

    for i in dca_log:
        i["date"] = i["date"].isoformat()

    content = {"ticker": ticker, "data": dca_log, "json_data": json.dumps(dca_log)}
    return render(request, "api/dollar_cost_average.html", content)
    return JsonResponse({"ticker": ticker, "data": dca_log})
