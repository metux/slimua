
class Mailbox:
    def __init__(self, name, mboxes = None):
        self.name   = name

        if mboxes is None:
            self.mboxes = {}
        else:
            self.mboxes = mboxes

    def get_mailboxes(self):
        return self.mboxes

    def add_mailbox(self, mbox, name = None):
        if name is None:
            name = mbox.name

        self.mboxes[name] = mbox
        return mbox
