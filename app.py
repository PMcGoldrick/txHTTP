from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint

from request import Request

class txHTTPProtocol(LineReceiver):
    """
    I am a protocol, analogous to a fork or a thread for traditional
    web servers
    """
    def __init__(self):
        self.request = Request()
        self.response = None

    def lineReceived(self, data):
        """
        Callback fired every time a new line (string terminated with \n \r or \n\r) is received
        """
        self.request.requestData = data
        # end of request
        if data == "":
            pass



class txHTTPFactory(Factory):
    """
    I am a factory, I spawn Protocols for every incoming connection
    """
    protocol = txHTTPProtocol


endpoint = TCP4ServerEndpoint(reactor, 8001)
endpoint.listen(txHTTPFactory())
reactor.run()