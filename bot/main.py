import re
from time import sleep

import requests

from pallegro.pallegro import AllegroWebApi


def launch_bot():
    allegro = init_allegro()
    user = login(allegro)

    print(user)
    huawei_id = allegro.get_user_id("SmA-Huawei1")
    print(huawei_id)
    print(allegro.get_user_public_data(user_id=huawei_id))

    while True:
        try:
            items = fetch_huawei_items()
            all_items = extract_all_products(items)
            print_all_items(all_items)
            desired_item_id, price = find_desired_item(all_items)
            if desired_item_id:
                print("BUYING DESIRED ITEM!!")
                for i in range(0, 50):
                    user.buy_or_bid(offer_id=desired_item_id, price=price, amount=1, buy_now=True)
                    sleep(0.01)
        except Exception:
            pass
        sleep(.01)


def extract_all_products(items):
    return [
        (item['id'], float(item['sellingMode']['price']['amount']), re.sub('[^A-Za-z0-9 ]+', '', item['name'].lower()))
        for item in items['items']['promoted'] + items['items']['regular']]


def print_all_items(all_items):
    for item in all_items:
        print(item)


def find_desired_item(all_items):
    for item in all_items:
        if 'honor' in item[2] and '7c' in item[2] and item[1] <= 10.0:
            print(item)
            return item[0], item[1]


def login(allegro):
    return allegro.login(USERNAME, PASSWORD)


def init_allegro():
    return AllegroWebApi(API_KEY, SANDBOX, COUNTRY)


def fetch_huawei_items():
    endpoint = 'https://api.allegro.pl/offers/listing?seller.id=47827759'
    headers = {"Authorization": "Bearer %s" % TOKEN, "Accept": "application/vnd.allegro.public.v1+json"}
    response = requests.get(endpoint, headers=headers)
    huawei_items = response.json()
    return huawei_items


if __name__ == '__main__':
    launch_bot()
