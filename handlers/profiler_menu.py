from services import get_profile as profile, get_blacklisted as blacklist
from helper import clear, colors, messages, translate

class ProfilerMenu:
    def menus():
        try:
            is_running = True

            while is_running:
                clear.clear_with_banner()

                print(translate.Translate().t("menu_title"))
                print(messages.line)
                print(f"{colors.yellow}1{colors.white} - {translate.Translate().t("menu_get_profile")}")
                print(f"{colors.yellow}2{colors.white} - {translate.Translate().t("menu_get_blacklisted")}")
                print(f"{colors.yellow}3{colors.white} - {translate.Translate().t("menu_exit")}")
                print(messages.line)

                choice = input(f'{translate.Translate().t("menu_input_data")} {colors.yellow}➜{colors.white}  ')

                if choice == '1':
                    clear.clear_with_banner()

                    server_ip = input(f'{translate.Translate().t("menu_input_server_id")} {colors.yellow}➜{colors.white}  ')
                    if not server_ip:
                        print(f'{colors.red}[-] {colors.white}{translate.Translate().t("menu_invalid_ip")}')
                        input(f'{colors.white}{translate.Translate().t("press_enter")}...')
                        continue

                    GetProfile = None

                    if "http://" in server_ip or "https://" in server_ip or "/" in server_ip:
                        server_ip = server_ip.replace("http://", "").replace("https://", "").split("/")
                        server_ip = server_ip[len(server_ip) - 1]
                        GetProfile = profile.GetProfile(server_ip, "id")

                    if ":" in server_ip:
                        GetProfile = profile.GetProfile(server_ip, "ip")

                    if GetProfile is None:
                        GetProfile = profile.GetProfile(server_ip, "id")

                    GetProfile.get()
                elif choice == '2':
                    clear.clear_with_banner()
                    blacklist.GetBlacklisted().get()
                elif choice == '3':
                    is_running = False
                    clear.clear_with_banner()
                    print(f"{translate.Translate().t("menu_thanks")} {colors.yellow}{translate.Translate().t("app_name")}{colors.white}!")
                else:
                    print(f'{colors.red}[-] {colors.white}{translate.Translate().t("menu_invalid_choice")}')
                    input(f'{colors.white}{translate.Translate().t("press_enter")}...')
        except KeyboardInterrupt:
            print(f'\n{colors.red}[-] {colors.white}{translate.Translate().t("menu_exiting")}...')
            exit()
