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
        items = fetch_huawei_items()
        all_items = [(item['id'], item['sellingMode']['price']['amount'], item['name'])
                     for item in items['items']['promoted'] + items['items']['regular']]
        for item in all_items:
            print(item)
        sleep(.5)


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
