import requests
from bs4 import BeautifulSoup
import datetime
import re


def get_yesterday_date():
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y-%m-%d")
    return yesterday_str


def get_stock_info(stock, date):
    headers = {"User-Agent": "Mozilla/5.0"}
    backend_url = f"https://sistemasweb.b3.com.br/PlantaoNoticias/Noticias/ListarTitulosNoticias?agencia=18&palavra={stock}&dataInicial={date}&dataFinal={date}"

    link_pattern = r"https://.*?ID=[0-9]+&flnk"

    res = requests.get(backend_url, headers=headers)
    res.json()

    for i in res.json():
        pdf_res = requests.get(
            f'https://sistemasweb.b3.com.br/PlantaoNoticias/Noticias/Detail?idNoticia={i["NwsMsg"]["id"]}&agencia={i["NwsMsg"]["IdAgencia"]}&dataNoticia={i["NwsMsg"]["dateTime"].replace(" ", "%20")}',
            headers=headers,
        )
        res_html = BeautifulSoup(pdf_res.text)
        res_html.find_all("pre")
        match = re.search(link_pattern, res_html.find_all("pre")[0].text.strip())
        if match:
            print(i["NwsMsg"]["headline"])
            print(match.group(0))


def get_news_link():
    pass


def get_pdf_link():
    pass


def main():
    stocks = [
        "bbdc",
        "taee",
        "unipar",
        "wizc",
        "hapv",
        "shul",
        "aure",
        "tris",
        "tasa",
        "klbn",
        "jhsf",
        "itub",
        "sapr",
        "cmig",
        "eletrobras",
        "bees",
        "bees",
        "bbas",
        "rani",
        "csmg",
        "petrobras",
        "irbr",
        "xpbr",
        "fesa",
    ]
    date = get_yesterday_date()
    for stock in stocks:
        get_stock_info(stock, date)
