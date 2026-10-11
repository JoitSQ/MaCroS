

class Security:
    def __init__(self, ui):
        from UInit import UI
        self.ui = ui
        self.publickey = None
        self.privatekey = None

    def Encrypt(self):
        if self.privatekey != self.publickey:
            self.ui.securitywarn.configure(text='End-to-End Encrypted.')
        if self.privatekey==self.publickey:
            self.ui.securitywarn.configure(text='Keys are matching. Security may be at risk.')