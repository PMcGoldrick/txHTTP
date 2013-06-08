class Response(object):
    """
    A default response object
    """
    def __init__(self, resp_code, body=None):
        self.resp_code = resp_code
        self.body = body
