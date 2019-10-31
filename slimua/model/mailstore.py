
from mailbox import MaildirMailstore
from mailbox import ImapMailstore

class Mailstore:
    def __init__(self, settings):
        self.settings  = settings
        self.accounts  = settings.get_accounts()
        self.mboxes    = {}
        self.drivers   = {
            'maildir': MaildirMailstore,
            'imap':    ImapMailstore,
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
