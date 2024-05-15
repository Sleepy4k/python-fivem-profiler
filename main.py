from time import sleep
from helper import translate
from handlers.profiler_menu import ProfilerMenu

class Main:
    def __init__(self):
        self._load()

    def _load(self):
        print(translate.Translate().t("welcome", translate.Translate().t("app_name"), "Python", "Benjamin4k"))
        print(f"{translate.Translate().t("loading")}...")
        sleep(2)
        ProfilerMenu.menus()

if __name__ == '__main__': Main()
else: print("This is a module, not a standalone script.")
