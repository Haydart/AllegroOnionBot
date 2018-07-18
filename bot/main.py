import requests

from pallegro.pallegro import AllegroWebApi


def launch_bot():
    allegro = init_allegro()
    user = login(allegro)

    print(user)
    # buy_request = user.buy_or_bid(offer_id=7445656286, price=5, amount=1, buy_now=True)
    huawei_id = allegro.get_user_id("SmA-Huawei1")
    print(huawei_id)
    print(allegro.get_user_public_data(user_id=huawei_id))

    fetch_huawei_auctions()


def login(allegro):
    return allegro.login(USERNAME, PASSWORD)


def init_allegro():
    return AllegroWebApi(API_KEY, SANDBOX, COUNTRY)


def fetch_huawei_auctions():
    endpoint = 'https://api.allegro.pl/offers/listing?seller.id=47827759'
    headers = {"Authorization": "Bearer %s" % TOKEN, "Accept": "application/vnd.allegro.public.v1+json"}
    response = requests.get(endpoint, headers=headers)
    huawei_auctions = response.json()
    print(huawei_auctions)
    return huawei_auctions


if __name__ == '__main__':
    launch_bot()
