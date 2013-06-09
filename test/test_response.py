from twisted.trial import unittest
from mock import Mock

from txHTTP.response import Response


class ResponseTestCase(unittest.TestCase):
    def setUp(self):
        self.response = Mock(spec=Response)

    def test_response_body_auto_populate(self, ):
        r = Response(404)
        self.assertIn("Not Found", r.render())
        self.assertIn("404", r.render())
