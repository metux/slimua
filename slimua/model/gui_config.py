import yaml

class GuiConfig:
    def __init__(self, spec):
        self.spec = spec

    def __getitem__(self, name):
        print("guiconfig: name="+name)
        if name in self.spec:
            return self.spec[name]
