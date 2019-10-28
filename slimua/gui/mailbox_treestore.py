from slimua.gui import Gtk

class MailboxTreeStore:

    def __init__(self, mailstore):
        self.mailstore = mailstore
        self.tree_store = Gtk.TreeStore(str)
        self.update()

    def update(self):
        self.counter = 0
        self.entries = []
        self.tree_store.clear()
        for n, m in self.mailstore.get_mailboxes().iteritems():
            self._add_mbox(None, n, m)

    def _add_mbox(self, parent, name, mbox):
        self.entries.append(mbox)
        ent = self.tree_store.append(parent, [name])
        self.counter = self.counter + 1
        for n, m in mbox.get_mailboxes().iteritems():
            self._add_mbox(ent, n, m)

    def get_store(self):
        return self.tree_store
