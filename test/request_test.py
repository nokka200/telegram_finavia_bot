import requests
import xml.etree.ElementTree as ET
from request_txt_test import flight_checker, flight_checker_2
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID_FINAVIA = os.getenv("APP_ID_FINAVIA")
APP_KEY_FINAVIA = os.getenv("APP_KEY_FINAVIA")

"""
This is the test file for the request moduele that will be used with the bot
"""


def requester(APP_ID_FINAVIA, APP_KEY_FINAVIA):

    head = {"app_id": APP_ID_FINAVIA, "app_key": APP_KEY_FINAVIA}
    url = "https://api.finavia.fi/flights/public/v0/flights/arr/HEL"

    re = requests.get(url, headers=head)

    re_str = re.text

    root = ET.fromstring(re_str)

    lenght = len(root[0][1][0])
    re_value = ""

    # print(root[0][1][0][0].text)

    # flight_checker(lenght, root)

    """
    for item in range(0, lenght):
        print(f"Lennon numero: {root[0][1][item][1].text}")
        print(f"Tila: {root[0][1][item][31].text}")
        print(f"Lähtö: (lähtö kaupunki)     {root[0][1][item][17].text}")
        print(f"33 est_d (arvioitu lähtö)   {root[0][1][item][33].text}")
        print(f"34 pest_d (todellinen lähtö){root[0][1][item][34].text}")
        print(f"35 act_d                    {root[0][1][item][35].text}")
        print(f"36 ablk_d                   {root[0][1][item][36].text}\n")

        re_value += f"Lennon numero: {root[0][1][item][1].text}\nTila: {root[0][1][item][31].text}\n"

    return re_value
    """

    final_re = flight_checker_2(lenght, root)
    return (final_re, lenght)


requester(APP_ID_FINAVIA, APP_KEY_FINAVIA)
