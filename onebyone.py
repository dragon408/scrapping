import requests
from bs4 import BeautifulSoup
import json

headers_rozetka = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}
page_rozetka = "https://rozetka.com.ua/ua/apple-mywv3sx-a/p448428614/"

response = requests.get(page_rozetka, headers=headers_rozetka)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    name = soup.find("meta", property="og:title")["content"]

    price = soup.find("p", class_="product-price__big product-price__big-color-red").text.strip()

    print(f"Назва товару: {name}")
    print(f"Ціна: {price}")

else:
    print("Не вдалося завантажити сторінку.")


###########################################


headers_foxtrot = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

page_foxtrot = "https://www.foxtrot.com.ua/uk/shop/smartfoniy-i-mobilniye-telefoniy-apple-iphone-16-pro-max-256gb-black-titanium.html?utm_source=google&utm_medium=cpc&utm_campaign=1-[regular]-[Srch]-[Pro]-[kw]-[API]-/dig/-UA%20_pr_mpc_reg_&utm_content=18515273183&gad_source=1&gclid=Cj0KCQiAgdC6BhCgARIsAPWNWH00oF8OyL4RGbRK8xlq4PXszGNjKawbvDBFPXG4ypbkLkpQABR6kk4aArJPEALw_wcB"

response = requests.get(page_foxtrot, headers=headers_foxtrot)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    script = soup.find("script", {"type": "application/ld+json"})

    if script:
        data = json.loads(script.string)

        if "hasVariant" in data:
            variant = data["hasVariant"][0]

            name = variant.get("name", "Не вказано")
            price = variant.get("offers", {}).get("price", "Не вказано")

            print(f"Назва товару: {name}")
            print(f"Ціна: {price} UAH")
        else:
            print("Варіанти не знайдені.")
else:
    print("Не вдалося завантажити сторінку.")


####################


headers_moyo = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

page_moyo = "https://www.moyo.ua/ua/smartfon_apple_iphone_16_pro_max_256gb_black_titanium/600492.html"

response = requests.get(page_moyo, headers=headers_moyo)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    title_tag = soup.find("meta", {"property": "og:title"})
    title = title_tag["content"] if title_tag else "Не вказано"

    price_tag = soup.find("meta", {"itemprop": "price"})
    price = price_tag["content"] if price_tag else "Не вказано"

    print(f"Назва товару: {title}")
    print(f"Ціна: {price} UAH")
else:
    print("Не вдалося завантажити сторінку.")


##########################


headers_ctrs = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

page_ctrs = "https://www.ctrs.com.ua/smartfony/iphone-16-pro-max-256gb-black-titanium-apple-752236.html"
page_ctrs = requests.get(page_ctrs, headers=headers_ctrs).text

soup = BeautifulSoup(page_ctrs, "html.parser")

price_element = soup.find("div", class_="Price_price__KKCnw")
if price_element:
    price = price_element.get("data-price", "Ціна не знайдена")
else:
    price = "Ціна не знайдена"

title_meta = soup.find("meta", {"property": "og:title"})
if title_meta:
    title = title_meta.get("content", "Назва не знайдена")
else:
    title = "Назва не знайдена"

print(f"Назва товару: {title}")
print(f"Ціна: {price} UAH")


############


headers_comfy = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}

page_comfy = "https://comfy.ua/ua/smartfon-apple-iphone-16-pro-max-256gb-black-titanium.html"
page_comfy = requests.get(page_comfy, headers=headers_comfy).text

soup = BeautifulSoup(page_comfy, "html.parser")

script_tag = soup.find("script", type="application/ld+json")
if script_tag:
    json_data = json.loads(script_tag.string)

    price = json_data.get("offers", {}).get("price", "Ціна не знайдена")

    title = json_data.get("name", "Назва не знайдена")

    print(f"Назва товару: {title}")
    print(f"Ціна: {price} UAH")

else:
    print("JSON-дані не знайдені.")
