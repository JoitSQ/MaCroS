class Networking():
    def __init__(self):
        self.TARGET_HOST = []
        self.TARGET_PORT = 54886
        self.HOST = ''

    def IPSetinit(self):
        self.target_host = ''
        with open(r"C:\MaCroS\P2PT\H-C\ipset.txt", 'r') as ipset:
            ippp = ipset.readlines()
            for i in range(len(ippp)):
                if i == 0:
                    self.host = ippp[i]
                else:
                    self.TARGET_HOST.append(ippp[i])
        for i in self.host:
            if i != '\n':
                self.HOST += i
