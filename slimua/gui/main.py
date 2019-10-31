from slimua.gui import Gtk, MainWindow

import signal
import sys

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    Gtk.main_quit()
#    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
#print('Press Ctrl+C')
#signal.pause()

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
        print("Goodbye")
