from config import lang as langconfig
import lang as langdata

class Translate:
    _lang = langconfig.LANGCONFIG["default"]

    def __init__(self, lang = None):
        if lang is not None: self._lang = lang

    def _parse(self, word, *args):
        for i in range(len(args)):
            word = word.replace(f"%{i + 1}", args[i])

        return word

    def get(self, key, *args):
        try:
            return self._parse(langdata.LANGUAGE[self._lang][key], *args)
        except KeyError:
            return langconfig.LANGCONFIG["missing"][self._lang].replace("%s", key)

    def translate(self, key, *args):
        return self.get(key, *args)

    def t(self, key, *args):
        return self.get(key, *args)

    def set_lang(self, lang):
        if lang in langconfig.LANGCONFIG["available"]:
            self._lang = lang
        else:
            print(f"Language {lang} not available.")
            exit()

    def get_lang(self):
        return self._lang

