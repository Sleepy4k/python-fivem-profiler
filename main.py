from handlers.profiler_menu import ProfilerMenu

class Main:
    def __init__(self):
        self._load()

    def _load(self):
        ProfilerMenu.menus()

if __name__ == '__main__': Main()
else: print("This is a module, not a standalone script.")
