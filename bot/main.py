from pallegro.pallegro import AllegroWebApi




def launch_bot():
    login_to_api()


def login_to_api():
    allegro_api = AllegroWebApi(API_KEY, SANDBOX, COUNTRY)
    user = allegro_api.login(USERNAME, PASSWORD)
    print(user)

    # buy_request = user.buy_or_bid(offer_id=7445656286, price=5, amount=1, buy_now=True)

    huawei_id = allegro_api.get_user_id("SmA-Huawei1")
    print(huawei_id)
    print(allegro_api.get_user_public_data(user_id=huawei_id))


if __name__ == '__main__':
    launch_bot()
