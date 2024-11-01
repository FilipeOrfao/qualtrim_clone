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
        # i["price"] = round(i["price"])

    dca_log = [
        {
            "date": "2017-01-31T00:00:00.000Z",
            "price": 58.70787811279297,
            "total_shares": 8.516744533661583,
            "total_investment": 500,
            "portfolio_value": 500.00000000000006,
        },
        {
            "date": "2017-04-29T23:00:00.000Z",
            "price": 62.544586181640625,
            "total_shares": 16.511041570785004,
            "total_investment": 1000,
            "portfolio_value": 1032.6762624726136,
        },
        {
            "date": "2017-07-30T23:00:00.000Z",
            "price": 66.79893493652344,
            "total_shares": 23.996190854604148,
            "total_investment": 1500,
            "portfolio_value": 1602.9199916211012,
        },
        {
            "date": "2017-10-31T00:00:00.000Z",
            "price": 76.83544158935547,
            "total_shares": 30.503604486352813,
            "total_investment": 2000,
            "portfolio_value": 2343.757920775963,
        },
        {
            "date": "2018-01-31T00:00:00.000Z",
            "price": 88.20389556884766,
            "total_shares": 36.17228835541985,
            "total_investment": 2500,
            "portfolio_value": 3190.536744587697,
        },
        {
            "date": "2018-04-29T23:00:00.000Z",
            "price": 87.22846221923828,
            "total_shares": 41.90436235144319,
            "total_investment": 3000,
            "portfolio_value": 3655.2530881941334,
        },
        {
            "date": "2018-07-30T23:00:00.000Z",
            "price": 99.37236022949219,
            "total_shares": 46.93594254985341,
            "total_investment": 3500,
            "portfolio_value": 4664.1353907747825,
        },
        {
            "date": "2018-10-31T00:00:00.000Z",
            "price": 100.44125366210938,
            "total_shares": 51.91397679146125,
            "total_investment": 4000,
            "portfolio_value": 5214.304911520018,
        },
        {
            "date": "2019-01-31T00:00:00.000Z",
            "price": 98.62741088867188,
            "total_shares": 56.98356135720016,
            "total_investment": 4500,
            "portfolio_value": 5620.141119876424,
        },
        {
            "date": "2019-04-29T23:00:00.000Z",
            "price": 123.87004089355469,
            "total_shares": 61.020049893033175,
            "total_investment": 5000,
            "portfolio_value": 7558.5560755767665,
        },
        {
            "date": "2019-07-30T23:00:00.000Z",
            "price": 129.72630310058594,
            "total_shares": 64.8743183648042,
            "total_investment": 5500,
            "portfolio_value": 8415.905487636497,
        },
        {
            "date": "2019-10-31T00:00:00.000Z",
            "price": 136.9398193359375,
            "total_shares": 68.52555729899186,
            "total_investment": 6000,
            "portfolio_value": 9383.877436418377,
        },
        {
            "date": "2020-01-31T00:00:00.000Z",
            "price": 163.1484832763672,
            "total_shares": 71.59025020914916,
            "total_investment": 6500,
            "portfolio_value": 11679.840738998315,
        },
        {
            "date": "2020-04-29T23:00:00.000Z",
            "price": 172.22398376464844,
            "total_shares": 74.49344632080845,
            "total_investment": 7000,
            "portfolio_value": 12829.558089727623,
        },
        {
            "date": "2020-07-30T23:00:00.000Z",
            "price": 197.56690979003906,
            "total_shares": 77.02423450052622,
            "total_investment": 7500,
            "portfolio_value": 15217.439989212278,
        },
        {
            "date": "2020-10-31T00:00:00.000Z",
            "price": 195.5908203125,
            "total_shares": 79.58059169152904,
            "total_investment": 8000,
            "portfolio_value": 15565.233209900287,
        },
        {
            "date": "2021-01-31T00:00:00.000Z",
            "price": 224.66554260253906,
            "total_shares": 81.80612211425417,
            "total_investment": 8500,
            "portfolio_value": 18379.016813008482,
        },
        {
            "date": "2021-04-29T23:00:00.000Z",
            "price": 244.81219482421875,
            "total_shares": 83.84850403219339,
            "total_investment": 9000,
            "portfolio_value": 20527.13630484862,
        },
        {
            "date": "2021-07-30T23:00:00.000Z",
            "price": 277.224609375,
            "total_shares": 85.65209571594487,
            "total_investment": 9500,
            "portfolio_value": 23744.86877700293,
        },
        {
            "date": "2021-10-30T23:00:00.000Z",
            "price": 323.2923889160156,
            "total_shares": 87.19868331634115,
            "total_investment": 10000,
            "portfolio_value": 28190.670639671043,
        },
        {
            "date": "2022-01-31T00:00:00.000Z",
            "price": 303.725341796875,
            "total_shares": 88.84490749059654,
            "total_investment": 10500,
            "portfolio_value": 26984.449894493173,
        },
        {
            "date": "2022-04-29T23:00:00.000Z",
            "price": 271.6063232421875,
            "total_shares": 90.68580719437169,
            "total_investment": 11000,
            "portfolio_value": 24630.83866231321,
        },
        {
            "date": "2022-07-30T23:00:00.000Z",
            "price": 275.397705078125,
            "total_shares": 92.50136335471863,
            "total_investment": 11500,
            "portfolio_value": 25474.663184487283,
        },
        {
            "date": "2022-10-31T00:00:00.000Z",
            "price": 228.196044921875,
            "total_shares": 94.69246180329682,
            "total_investment": 12000,
            "portfolio_value": 21608.445267428055,
        },
        {
            "date": "2023-01-31T00:00:00.000Z",
            "price": 244.29684448242188,
            "total_shares": 96.73915217729376,
            "total_investment": 12500,
            "portfolio_value": 23633.069614817676,
        },
        {
            "date": "2023-04-29T23:00:00.000Z",
            "price": 303.6627502441406,
            "total_shares": 98.38571567445635,
            "total_investment": 13000,
            "portfolio_value": 29876.07700644347,
        },
        {
            "date": "2023-07-30T23:00:00.000Z",
            "price": 332.71295166015625,
            "total_shares": 99.88851259746498,
            "total_investment": 13500,
            "portfolio_value": 33234.201863245275,
        },
        {
            "date": "2023-10-31T00:00:00.000Z",
            "price": 335.5910339355469,
            "total_shares": 101.37842129417953,
            "total_investment": 14000,
            "portfolio_value": 34021.68922086717,
        },
        {
            "date": "2024-01-31T00:00:00.000Z",
            "price": 395.4189147949219,
            "total_shares": 102.64290304073259,
            "total_investment": 14500,
            "portfolio_value": 40586.94533176687,
        },
        {
            "date": "2024-04-29T23:00:00.000Z",
            "price": 387.9298095703125,
            "total_shares": 103.93179599936812,
            "total_investment": 15000,
            "portfolio_value": 40318.24183033544,
        },
        {
            "date": "2024-07-30T23:00:00.000Z",
            "price": 417.5973205566406,
            "total_shares": 105.12912168942168,
            "total_investment": 15500,
            "portfolio_value": 43901.63952997551,
        },
        {
            "date": "2024-10-31T00:00:00.000Z",
            "price": 431.95001220703125,
            "total_shares": 106.28666303881364,
            "total_investment": 16000,
            "portfolio_value": 45910.52539706017,
        },
    ]

    content = {"ticker": ticker, "data": dca_log, "json_data": json.dumps(dca_log)}
    return render(request, "api/dollar_cost_average.html", content)
    return JsonResponse({"ticker": ticker, "data": dca_log})
