from slimua.gui import Gtk
from pprint import pprint

class MailboxTreeStore:

    def __init__(self, mailstore):
        self.mailstore = mailstore
        self.tree_store = Gtk.TreeStore(str, object)
        self.update()

    def update(self):
        self.entries = []
        self.tree_store.clear()
        for n, m in self.mailstore.get_mailboxes().iteritems():
            self._add_mbox(None, n, m)

    def _add_mbox(self, parent, name, mbox):
        self.entries.append(mbox)
        ent = self.tree_store.append(parent, [name, mbox])
        for n, m in mbox.get_mailboxes().iteritems():
            self._add_mbox(ent, n, m)

    def get_store(self):
        return self.tree_store

    def get_by_path(self, path):
        l = self.mailstore.get_mailboxes()
        for n in path:
            print "path elem: "+str(n)
            pprint(l[n])
