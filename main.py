from bs4 import BeautifulSoup
import requests
from forex_python.converter import CurrencyRates
from Make_graph import make_graph

link_usa = "https://www2.hm.com/en_us/men/products/t-shirts-tank-tops.html?sort=stock&image-size=small&image=model&offset=0&page-size=1000"
link_canada = "https://www2.hm.com/en_ca/men/shop-by-product/t-shirts-and-tank-tops.html?sort=stock&image-size=large&image=model&offset=0&page-size=100"
link_espanyol = "https://www2.hm.com/es_es/hombre/compra-por-producto/camisetas-de-manga-corta-y-sin-mangas.html?sort=stock&image-size=large&image=model&offset=0&page-size=1000"
link_turkey = "https://www2.hm.com/tr_tr/erkek/urune-gore-satin-al/tisort-atlet.html?sort=stock&image-size=small&image=stillLife&offset=0&page-size=1000"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def transfer_currency(currency1, currency2, price):
    currency = CurrencyRates()
    rate = currency.get_rate(currency1, currency2)
    return price * rate


def get_data(country_link):
    html_text = requests.get(country_link, headers=headers).content.decode()

    soup = BeautifulSoup(html_text, "lxml")
    prices = soup.find_all("span", class_="price")

    counter = 0
    total_price = 0
    for price in prices:
        counter += 1
        text = price.text.replace(",", ".")
        if text.startswith("$"):
            float_price = float(text.replace("$", ""))
            total_price += float_price

        elif text.endswith("€"):
            float_price = float(text.replace("€", ""))
            total_price += float_price
        elif text.endswith("TL"):
            float_price = float(text.replace("TL", ""))
            total_price += float_price

    return (total_price / counter)


turkey = transfer_currency("TRY","USD",get_data(link_turkey))
usa = get_data(link_usa)
canada = get_data(link_canada)
espanyol = transfer_currency("EUR","USD",get_data(link_espanyol))

averages = [turkey,usa,canada,espanyol]
countries = ["Turkey","Usa","Canada","Spain"]
make_graph(countries,averages,"Countries","Prices($)","H&M Man Tshirt Index")
