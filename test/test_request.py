from twisted.trial import unittest
from mock import Mock

from txHTTP.request import Request


class RequestTestCase(unittest.TestCase):
    def setUp(self):
        self.request = Mock(spec=Request)
        self.request_lines = ["GET / HTTP/1.1",
                            "Host: localhost:8001",
                            "Connection: keep-alive",
                            "Cache-Control: max-age=0",
                            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                            "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.110 Safari/537.36",
                            "Referer: http://localhost:8001/",
                            "Accept-Encoding: gzip,deflate,sdch",
                            "Accept-Language: en-US,en;q=0.8",
                            ""
                            ]


    def test_add_line_to_request_object(self):
        self.request._raw_request = []
        self.request.requestData = Request.requestData
        for line in self.request_lines:
            self.request.requestData.__set__(self.request, line)

        self.assertEqual(self.request.requestData.__get__(self.request), "\r\n".join(self.request_lines))
