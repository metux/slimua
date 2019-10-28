from slimua.gui import Gtk, MainWindow

class AskPass:
    def __init__(self):
        self.dummy = 0

class Main:
    def __init__(self, settings, mailstore):
        self.settings = settings
        self.mailstore = mailstore

    def run(self):
        win = MainWindow(settings = self.settings, mailstore = self.mailstore)
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        win.maximize()
        Gtk.main()
