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