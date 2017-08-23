#! /usr/bin/python
from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 8099
ADDR = (HOST, PORT)


class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = input('>:')
        if data:
            print('....sending %s' % data)
            self.transport.write(data.encode())
        else:
            self.tramsport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data)
        self.sendData()


class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()


reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()