from slimua.gui import Gtk, MailboxTreeView, MailboxTreeStore

class MainWindow(Gtk.Window):

    def get_mailbox_tree(self):
        return self.tree_store

    def activate_mailbox(self, name):
        print ("master: mailbox activated: "+name)

    def __init__(self, settings, mailstore):
        Gtk.Window.__init__(self, title="SliMUA")

        self.settings = settings
        self.mailstore = mailstore

        self.mailbox_tree_store = MailboxTreeStore(mailstore)
        self.mailbox_tree_view  = MailboxTreeView(self, treestore = self.mailbox_tree_store)
        self.message_view       = Gtk.TextView()
        self.index_view         = Gtk.TextView()

        self.vpaned = Gtk.VPaned()
        self.vpaned.add1(self.index_view)
        self.vpaned.add2(self.message_view)

        self.hpaned = Gtk.HPaned()
        self.hpaned.set_position(2000)
        self.hpaned.add1(self.mailbox_tree_view.get_widget())
        self.hpaned.add2(self.vpaned)
        self.hpaned.set_position(self.settings['gui.mainwindow.hsplit'])
        self.add(self.hpaned)

        print "hsplit="+str(self.settings['gui.mainwindow.hsplit'])
        self.hpaned.set_position(2000)

    def select_mailbox(self, mbox):
        print ("MainWindow: user selected mailbox: "+mbox.name)
        self.index_view.get_buffer().set_text("MainWindow: user selected mailbox: "+mbox.name)
