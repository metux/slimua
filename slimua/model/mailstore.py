
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

class MaildirMailstore(Mailbox):
    def __init__(self, name, spec):
        Mailbox.__init__(self, name)
        self.spec = spec
        self.mboxes = {}

        inbox = self.add_mailbox(Mailbox('Inbox'))
        outbox = self.add_mailbox(Mailbox('Outbox'))
        sent = self.add_mailbox(Mailbox('Sent'))
        drafts = self.add_mailbox(Mailbox('Drafts'))

        one = inbox.add_mailbox(Mailbox('One'))
        two = one.add_mailbox(Mailbox('Two'))

class Mailstore:
    def __init__(self, settings):
        self.settings  = settings
        self.accounts  = settings.get_accounts()
        self.mboxes    = {}
        self.drivers   = {
            'maildir': MaildirMailstore,
        }

        for ac in self.accounts:
            account = self.accounts[ac]
            dn = account['driver']
            if dn in self.drivers:
                self.mboxes[ac] = self.drivers[dn](ac, account)
            else:
                print("missing mailbox driver: "+dn)

    def get_mailboxes(self):
        return self.mboxes
