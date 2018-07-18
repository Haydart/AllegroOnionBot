import os

from pallegro.pallegro import AllegroWebApi

API_KEY = os.environ["ALLEGRO_API_KEY"]
COUNTRY = 'PL'
SANDBOX = True
USERNAME = os.environ["ALLEGRO_USERNAME"]
PASSWORD = os.environ["ALLEGRO_PASSWORD"]


def launch_bot():
    login_to_api()


def login_to_api():
    allegro_api = AllegroWebApi(API_KEY, SANDBOX, COUNTRY)
    user = allegro_api.login(USERNAME, PASSWORD)
    # print(user)


if __name__ == '__main__':
    launch_bot()
