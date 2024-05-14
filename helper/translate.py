from config import lang as langconfig
import lang as langdata

class Translate:
    _lang = langconfig.LANGCONFIG["default"]

    def __init__(self, lang = None):
        if lang is not None: self._lang = lang

    def get(self, key):
        try:
            return langdata.LANGUAGE[self._lang][key]
        except KeyError:
            return langconfig.LANGCONFIG["missing"][self._lang].replace("%s", key)

    def translate(self, key):
        return self.get(key)

    def t(self, key):
        return self.get(key)
