from pallegro.pallegro import AllegroWebApi



def launch_bot():
    login_to_api()


def login_to_api():
    allegro_api = AllegroWebApi(API_KEY, SANDBOX, COUNTRY)
    user = allegro_api.login(USERNAME, PASSWORD)
    buy_request = user.buy_or_bid(offer_id=7445656286, price=5, amount=1, buy_now=True)
    print(user)
    print(buy_request)


if __name__ == '__main__':
    launch_bot()
