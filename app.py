from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint

from request import Request
from response import Response
from common import status_codes

def txHTTPMethodNotImplemented(f):
    """
    Decorator to return Not Implemented to a client
    """
    def replacement(*args, **kwargs):
        print "unimplemented method {} called".format(f.__name__)
        return Response(501)
    return replacement

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
            self.request.processRequest()
            resp = getattr(self, "handle" + self.request.method, self.handleERROR)()
            self.transport.write(resp.render())
            self.transport.loseConnection()

    @txHTTPMethodNotImplemented
    def handleGET(self):
        pass

    @txHTTPMethodNotImplemented
    def handlePOST(self):
        pass

    @txHTTPMethodNotImplemented
    def handlePUT(self):
        pass

    @txHTTPMethodNotImplemented
    def handleDELETE(self):
        pass

    @txHTTPMethodNotImplemented
    def handleERROR(self):
        pass

class txHTTPFactory(Factory):
    """
    I am a factory, I spawn Protocols for every incoming connection
    """
    protocol = txHTTPProtocol


endpoint = TCP4ServerEndpoint(reactor, 8001)
endpoint.listen(txHTTPFactory())
reactor.run()