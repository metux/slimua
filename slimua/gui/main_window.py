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
        self.mailbox_tree_view = MailboxTreeView(self, treestore = self.mailbox_tree_store)

        self.vp = Gtk.HPaned()
        self.vp.set_position(2000)
        self.vp.add1(self.mailbox_tree_view.get_widget())
        self.tv = Gtk.TextView()
        self.vp.add2(self.tv)
        self.vp.set_position(self.settings['gui.mainwindow.hsplit'])
        self.add(self.vp)

        print "hsplit="+str(self.settings['gui.mainwindow.hsplit'])
        self.vp.set_position(2000)

    def select_mailbox(self, mbox):
        print ("MainWindow: user selected mailbox: "+mbox.name)
        self.tv.get_buffer().set_text("MainWindow: user selected mailbox: "+mbox.name)
