import requests as req
import http.client as http
from time import sleep
from helper import messages, translate

class GetProfile:
    # This variable is protected and can be accessed within the class and its subclasses.
    _ip = None

    # This variable is private and can only be accessed within the class.
    __headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "sec-ch-ua": '"Chromium";v="96", "Opera GX";v="82", ";Not A Brand";v="99"',
        "origin": "https://servers.fivem.net",
        "referer": "https://servers.fivem.net/",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.25"
    }

    def __init__(self, ip):
        self._ip = ip

    def __get_profile(self):
        try:
            response = req.get(f"https://servers-frontend.fivem.net/api/servers/single/{self._ip}", headers=self.__headers)

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
        if isinstance(header, dict):
            for key, value in header.items():
                self.__headers[key] = value

    def get(self):
        print(f"{translate.Translate().t("profile_get_ready")} {self._ip}...")
        sleep(2)

        profile = self.__get_profile()

        if "error" in profile:
            print(f"{translate.Translate().t("profile_error")}: {profile['error']}")
            print(f"{translate.Translate().t("profile_message")}: {profile['message']}")
            input(f'{translate.Translate().t("press_enter")}...')
            return None

        sv_endpoint = profile["Data"]["connectEndPoints"][0]
        sv_endpoint_cfx = profile["EndPoint"]
        sv_max_players = profile["Data"]["svMaxclients"]
        sv_gamebuild = profile["Data"]["vars"]['sv_enforceGameBuild']
        sv_request_steam_ticket = profile["Data"]['requestSteamTicket']
        sv_desc = profile['Data']['vars']['sv_projectDesc']
        sv_origin = profile['Data']['server']
        sv_clients = profile['Data']['clients']
        sv_keymaster_token = profile['Data']['vars']['sv_licenseKeyToken'].split(":")[0]
        sv_keymaster_id = profile['Data']['vars']['sv_licenseKeyToken'].split(":")[1]
        sv_owner_id = profile['Data']['ownerID']
        sv_owner_name = profile['Data']['ownerName']
        sv_owner_avatar = profile['Data']['ownerAvatar']
        sv_owner_profile = profile['Data']['ownerProfile']
        sv_resources = profile['Data']['resources']

        print(f'{messages.line}')
        print(f'{messages.title} {translate.Translate().t("profile_server_info")}  {messages.title}')
        print(f'{messages.title} {translate.Translate().t("profile_server_ip")} {messages.arrow}  {sv_endpoint}')

        sleep(1)

        print(f'{messages.title} {translate.Translate().t("profile_cfx_endpoint")} {messages.arrow}  {sv_endpoint_cfx}')
        print(f'{messages.title} {translate.Translate().t("profile_request_steam_ticket")} {messages.arrow}  {sv_request_steam_ticket}')
        print(f'{messages.title} {translate.Translate().t("profile_server_max_client")} {messages.arrow}  {sv_max_players}')
        print(f'{messages.title} {translate.Translate().t("profile_server_game_build")} {messages.arrow}  {sv_gamebuild}')
        print(f'{messages.title} {translate.Translate().t("profile_server_description")} {messages.arrow}  {sv_desc}')
        print(f'{messages.title} {translate.Translate().t("profile_server_origin")} {messages.arrow}  {sv_origin}')
        print(f'{messages.title} {translate.Translate().t("profile_server_online_player")} {messages.arrow}  {sv_clients}')
        print(f'{messages.line}')
        print(f'{messages.title} {translate.Translate().t("profile_keymaster")}  {messages.title}')
        print(f'{messages.title} {translate.Translate().t("profile_keymaster_token")} {messages.arrow}  {sv_keymaster_token}')
        print(f'{messages.title} {translate.Translate().t("profile_keymaster_id")} {messages.arrow}  {sv_keymaster_id}')
        print(f'{messages.line}')
        print(f'{messages.title} {translate.Translate().t("profile_owner")}  {messages.title}')
        print(f'{messages.title} {translate.Translate().t("profile_owner_id")} {messages.arrow}  {sv_owner_id}')
        print(f'{messages.title} {translate.Translate().t("profile_owner_name")} {messages.arrow}  {sv_owner_name}')
        print(f'{messages.title} {translate.Translate().t("profile_owner_avatar")} {messages.arrow}  {sv_owner_avatar}')
        print(f'{messages.title} {translate.Translate().t("profile_owner_profile")} {messages.arrow}  {sv_owner_profile}')
        print(f'{messages.line}')

        confirmation = input(f'{translate.Translate().t("profile_reso_confirm")} (yes/no) {messages.arrow}  ')

        if confirmation.lower() == 'yes' or confirmation.lower() == 'y':
            print(f'{messages.title} {translate.Translate().t("profile_server_resources")}  {messages.title}')
            for resource in sv_resources:
                print(f'{messages.title} {messages.arrow}  {resource}')
        else:
            print(f'{messages.title} {translate.Translate().t("profile_server_resources")} {messages.arrow}  {translate.Translate().t("profile_resource_not_shown")}')

        input(f'{translate.Translate().t("press_enter")}...')
