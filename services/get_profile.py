import requests as req
import http.client as http
from time import sleep
from helper import messages, translate

class GetProfile:
    # This variable is protected and can be accessed within the class and its subclasses.
    _ip = None
    _type = None

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

    def __init__(self, ip, type = "id"):
        self._ip = ip
        self._type = type

    def __hit_endpoint_by_id(self):
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

    def __hit_endpoint_by_ip(self):
        try:
            response = None

            info_response = req.get(f"http://{self._ip}/info.json", headers=self.__headers)

            if info_response.status_code == http.OK: response = info_response.json()
            else: return {
                    "error": info_response.status_code,
                    "message": info_response.reason
                }

            dynamic_response = req.get(f"http://{self._ip}/dynamic.json", headers=self.__headers)

            if dynamic_response.status_code == http.OK: response["clients"] = dynamic_response.json()["clients"]
            else: return {
                    "error": dynamic_response.status_code,
                    "message": dynamic_response.reason
                }

            return response
        except req.exceptions.RequestException as e:
            return {
                "error": 500,
                "message": str(e)
            }

    def __get_profile(self):
        body = None

        if self._type == "id": body = self.__hit_endpoint_by_id()
        else: body = self.__hit_endpoint_by_ip()

        if body is None:
            return {
                "error": 500,
                "message": "No response from the server."
            }

        if "error" in body:
            return {
                "error": body["error"],
                "message": body["message"]
            }

        if self._type == "id":
            return {
                "sv_endpoint": body["Data"]["connectEndPoints"][0],
                "sv_endpoint_cfx": body["EndPoint"],
                "sv_max_players": body["Data"]["svMaxclients"],
                "sv_gamebuild": body["Data"]["vars"]['sv_enforceGameBuild'],
                "sv_request_steam_ticket": body["Data"]['requestSteamTicket'],
                "sv_desc": body['Data']['vars']['sv_projectDesc'],
                "sv_origin": body['Data']['server'],
                "sv_clients": body['Data']['clients'],
                "sv_keymaster_token": body['Data']['vars']['sv_licenseKeyToken'].split(":")[0] if body['Data']['vars']['sv_licenseKeyToken'] else "N/A",
                "sv_keymaster_id": body['Data']['vars']['sv_licenseKeyToken'].split(":")[1] if body['Data']['vars']['sv_licenseKeyToken'] else "N/A",
                "sv_owner_id": body['Data']['ownerID'],
                "sv_owner_name": body['Data']['ownerName'],
                "sv_owner_avatar": body['Data']['ownerAvatar'],
                "sv_owner_profile": body['Data']['ownerProfile'],
                "sv_resources": body['Data']['resources'],
            }
        else:
            return {
                "sv_endpoint": self._ip,
                "sv_max_players": body["vars"]["sv_maxClients"],
                "sv_gamebuild": body["vars"]['sv_enforceGameBuild'],
                "sv_request_steam_ticket": body['requestSteamTicket'],
                "sv_desc": body['vars']['sv_projectDesc'],
                "sv_origin": body['server'],
                "sv_clients": body['clients'],
                "sv_keymaster_token": body['vars']['sv_licenseKeyToken'].split(":")[0] if body['vars']['sv_licenseKeyToken'] else "N/A",
                "sv_keymaster_id": body['vars']['sv_licenseKeyToken'].split(":")[1] if body['vars']['sv_licenseKeyToken'] else "N/A",
                "sv_resources": body['resources'],
            }

    def override_headers(self, header):
        if isinstance(header, dict):
            for key, value in header.items():
                self.__headers[key] = value

    def get(self):
        print(f"{translate.Translate().t("profile_get_ready")} {self._ip}...")
        sleep(2)

        profile = self.__get_profile()

        if profile is None: return
        elif "error" in profile:
            print(f"{translate.Translate().t("profile_error")}: {profile['error']}")
            print(f"{translate.Translate().t("profile_message")}: {profile['message']}")
            input(f'{translate.Translate().t("press_enter")}...')
            return

        sv_endpoint = profile["sv_endpoint"] if "sv_endpoint" in profile else "N/A"
        sv_endpoint_cfx = profile["sv_endpoint_cfx"] if "sv_endpoint_cfx" in profile else "N/A"
        sv_max_players = profile["sv_max_players"] if "sv_max_players" in profile else "N/A"
        sv_gamebuild = profile["sv_gamebuild"] if "sv_gamebuild" in profile else "N/A"
        sv_request_steam_ticket = profile["sv_request_steam_ticket"] if "sv_request_steam_ticket" in profile else "N/A"
        sv_desc = profile['sv_desc'] if 'sv_desc' in profile else "N/A"
        sv_origin = profile['sv_origin'] if 'sv_origin' in profile else "N/A"
        sv_clients = profile['sv_clients'] if 'sv_clients' in profile else "N/A"
        sv_keymaster_token = profile['sv_keymaster_token'] if 'sv_keymaster_token' in profile else "N/A"
        sv_keymaster_id = profile['sv_keymaster_id'] if 'sv_keymaster_id' in profile else "N/A"
        sv_owner_id = profile['sv_owner_id'] if 'sv_owner_id' in profile else "N/A"
        sv_owner_name = profile['sv_owner_name'] if 'sv_owner_name' in profile else "N/A"
        sv_owner_avatar = profile['sv_owner_avatar'] if 'sv_owner_avatar' in profile else "N/A"
        sv_owner_profile = profile['sv_owner_profile'] if 'sv_owner_profile' in profile else "N/A"
        sv_resources = profile['sv_resources'] if 'sv_resources' in profile else "N/A"

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
