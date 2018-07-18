from pallegro.pallegro import AllegroWebApi

API_KEY = 'a6f31c8c587740d796de5c6c6e01dadc'
COUNTRY = 'PL'
SANDBOX = False
USERNAME = 'radmack'
PASSWORD = 'SyncMaster14'
TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MzE5NDQ5NjgsInVzZXJfbmFtZSI6IjI4MTczNDc2IiwianRpIjoiMzczMDllYTMtZTM3ZS00M2NjLTk2ODMtMjg1NDViYmZjOTRiIiwiY2xpZW50X2lkIjoiYTZmMzFjOGM1ODc3NDBkNzk2ZGU1YzZjNmUwMWRhZGMiLCJzY29wZSI6WyJhbGxlZ3JvX2FwaSJdfQ.VWqWz2Yl-D83dii-VDOwxbUfX9gP7BJe1v4UA70lQ4MtY5bXVRI_4L--aAtyReQoESOq1N0A1IvTTJ1lwA13BA5yxuJfmjvNuIdwpi46fIP9FGXR2SLIQHoNIKncOMRVVVtVShJMz8a5r04Dj2xBM7ngYbEEjT5krbbZh_LnjkvfJGOQ4zqE-9Qafwf5Jg3WzYWhuFzkISzlk5-_0x8DcY8TB6VRisN6Ryb3uborcvkNwjmRzBEqq9-yWRmvjBjt6WRYaU3hqoMi6xOwrjZVTt0mj01IEeS9GDZBpuxVF5O0ZyNLrAYpYA0bUDNPfpSYpHL9zUShSlqOCgQPkFD_Cg'


def launch_bot():
    allegro = init_allegro()
    user = login(allegro)

    print(user)
    # buy_request = user.buy_or_bid(offer_id=7445656286, price=5, amount=1, buy_now=True)
    huawei_id = allegro.get_user_id("SmA-Huawei1")
    print(huawei_id)
    print(allegro.get_user_public_data(user_id=huawei_id))


def login(allegro):
    return allegro.login(USERNAME, PASSWORD)


def init_allegro():
    return AllegroWebApi(API_KEY, SANDBOX, COUNTRY)


if __name__ == '__main__':
    launch_bot()
