from .colors import *
from .translate import Translate

def banner():
    print(f"""
 ____             _                 _      _  _   _
|  _ \           (_)               (_)    | || | | |
| |_) | ___ _ __  _  __ _ _ __ ___  _ _ __| || |_| | __
|  _ < / _ \ '_ \| |/ _` | '_ ` _ \| | '_ \__   _| |/ /
| |_) |  __/ | | | | (_| | | | | | | | | | | | | |   <
|____/ \___|_| |_| |\__,_|_| |_| |_|_|_| |_| |_| |_|\_\\
                _/ |
                |__/                                      {yellow}~{white} {Translate().t("app_name")} v1.0

{yellow}#{white} Info
    """)
