import requests as req
import http.client as http
from time import sleep
from helper import messages, translate

class GetBlacklisted:
    # This variable is private and can only be accessed within the class.
    __headers = {
        "accept": "*/*",
        "host": "runtime.fivem.net",
        "user-agent": "CitizenFX/1"
    }

    def __get_blacklisted(self):
        try:
            response = req.get("https://runtime.fivem.net/nui-blacklist.json", headers=self.__headers)

            if response.status_code == http.OK: return response.json()
            else: return {
                    "error": response.status_code,
                    "message": response.reason
                }
        except req.exceptions.RequestException as e:
            return {
                "error": 500,
                "message": str(e)
            }

    def override_headers(self, header):
        """Check if the header is a dictionary and override the default headers."""
        if isinstance(header, dict):
            for key, value in header.items():
                self.__headers[key] = value
        else:
            print(f"{translate.Translate().t('blacklist_invalid_header')}")

    def get(self):
        print(f"{translate.Translate().t("blacklist_get_ready")}...")
        sleep(2)

        data = self.__get_blacklisted()

        if "error" in data:
            print(f"{translate.Translate().t("blacklist_error")}: {data['error']}")
            print(f"{translate.Translate().t("blacklist_message")}: {data['message']}")
            input(f'{translate.Translate().t("press_enter")}...')
            return None

        print(f'{messages.line}')
        for value in data:
            print(f'{messages.arrow} {value}')
        print(f'{messages.line}')

        input(f'{translate.Translate().t("press_enter")}...')
