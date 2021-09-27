import requests
import xml.etree.ElementTree as ET


class Finavia_request:
    def __init__(self, APP_ID_FINAVIA, APP_KEY_FINAVIA):
        self.APP_ID_FINAVIA = APP_ID_FINAVIA
        self.APP_KEY_FINAVIA = APP_KEY_FINAVIA
        self.status = "arr"
        self.airport = "HEL"
        self.url = f"https://api.finavia.fi/flights/public/v0/flights/{self.status}/{self.airport}"

    def __str__(self):
        return f"app_id: {self.APP_ID_FINAVIA}\napp_key: {self.APP_KEY_FINAVIA}"

    def get_head(self, id="app_id", key="app_key"):
        # returns the headers that will be used to acces finavia api
        return {id: self.APP_ID_FINAVIA, key: self.APP_KEY_FINAVIA}

    def get_xml_root(self, headers, to_text=True, file=""):
        # returns the xml root using request GET, option to add it from text file

        if to_text:
            re_request = requests.get(self.url, headers=headers)
            re_request_text = re_request.text
            root = ET.fromstring(re_request_text)
            return root
        else:
            tree = ET.parse(file)
            root = tree.getroot()
            return root

    def get_xml_lenght(self, root):
        # gets the lenght on spot [0][1][0] which is the number of flights

        lenght = len(root[0][1][0])
        return lenght
