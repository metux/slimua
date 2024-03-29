import yaml

from account_config import AccountConfig
from gui_config import GuiConfig

class Settings:
    def __init__(self):
        self.settings = {
            'gui.mainwindow.hsplit':    800,
        }
        self.accounts = None
        self.guiconf = None

    def get_accounts(self):
        if self.accounts is None:
            self.accounts = AccountConfig(self.__load_cf_yaml('accounts.yml'))
        return self.accounts

    def get_guiconf(self):
        if self.guiconf is None:
            self.guiconf = GuiConfig(self.__load_cf_yaml('gui.yml'))
        return self.guiconf

    def __load_cf_yaml(self, name):
        fn = self['config.prefix']+"/"+name

        with open(fn, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return {}

    def __getitem__(self, attr):
        return self.settings.get(attr, None)

    def __setitem__(self, attr, val):
        self.settings[attr] = val
