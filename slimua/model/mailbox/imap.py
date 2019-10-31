
from slimua.model.mailbox.mailbox import Mailbox

import imaplib
import pprint

def parse_mailbox(data):
    print "RAW: "+data
    flags, b, c = data.partition(' ')
    separator, b, name = c.partition(' ')
    return (flags, separator.replace('"', ''), name.replace('"', ''))

class ImapMailstore(Mailbox):
    def __init__(self, name, account):
        Mailbox.__init__(self, name)
        self.account = account
        self.mboxes = {}

        pprint.pprint(self.account.spec)
        server = self.account['server']
        port = self.account['port']
        username = self.account['username']
        passwd = self.account['passwd']

        # connect to host using SSL
        self.connection = imaplib.IMAP4_SSL(server)

        ## login to server
        self.connection.login(username, passwd)

#        mboxlist = self.connection.list()
#        pprint.pprint(mboxlist)

        resp, data = self.connection.list('""', '*')
        if resp == 'OK':
            for mbox in data:
                flags, separator, name = parse_mailbox(bytes.decode(mbox))
                fmt = '==> "{0}"           : [Flags = "{1}"; Separator = "{2}"'
                print(fmt.format(name, flags, separator))

#        self.connection.select('Inbox')
#        tmp, data = self.connection.search(None, 'ALL')
#        for num in data[0].split():
#            tmp, data = self.connection.fetch(num, '(RFC822)')
#            print('Message: {0}\n'.format(num))
#            pprint.pprint(data[0][1])
#            break
#        self.connection.close()

#        inbox = self.add_mailbox(Mailbox('Inbox'))
#        outbox = self.add_mailbox(Mailbox('Outbox'))
#        sent = self.add_mailbox(Mailbox('Sent'))
#        drafts = self.add_mailbox(Mailbox('Drafts'))
#
#        one = inbox.add_mailbox(Mailbox('One'))
#        two = one.add_mailbox(Mailbox('Two'))
