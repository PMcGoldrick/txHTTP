class Request(object):
    """
    I am trying to be an HTTP request
    """
    def __init__(self):
        self._raw_request = []
        self.method = None
        self.uri = None
        self.version = None
        self.get_params = {}

    @property
    def requestData(self):
        """
        For now we'll just use this to add new data to the raw_request list
        """
        pass

    @requestData.setter
    def requestData(self, data):
        """
        Append data to our request data list
        """
        self._raw_request.append(data)

    @requestData.getter
    def requestData(self):
        return "\r\n".join(self._raw_request)

    def processRequest(self,):
        """
        Parse the request data sent from the client
        """
        # We really only care about the status line for this
        self.method, self.uri, self.version = self._raw_request[0].split(" ")
        if self.method == "GET":
            self.parseUri()

    def parseUri(self):
        """
        Parse get parameters if there are any
        """
        if "?" in self.uri:
            self.uri, tmp = self.uri.split("?")
            tmp = tmp.split("&")
            for kv in tmp:
                k, v = kv.split("=")
                self.get_params[k] = v
