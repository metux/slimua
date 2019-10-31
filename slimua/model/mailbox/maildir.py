
from slimua.model.mailbox import Mailbox

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
