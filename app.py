from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory

class txHTTPProtocol(LineReceiver):
    """
    I am a protocol, analogous to a fork or a thread for traditional
    web servers
    """
    pass

class txHTTPFactory(Factory):
    """
    I am a factory, I spawn Protocols for every incoming connection
    """
    protocol = txHTTPProtocol


endpoint = TCP4ServerEndpoint(reactor, 8001)
endpoint.listen(NotSecureFactory())
reactor.run()