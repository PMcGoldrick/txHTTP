from common import status_codes

class Response(object):
    """
    A default response object
    """
    def __init__(self, resp_code, body=None):
        self.resp_code = resp_code
        self.body = body
        self.doctype = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">"""
        # Set the status text as the <body> if `body` isn't specified
        if not self.body:
            self.body = """<html>
                            <head>
                                <title>{}</title>
                            </head>
                            <body>{}</body>
                        </html>
                        """.format(str(self.resp_code), status_codes[int(self.resp_code)])

        self.headers = {
            'Content-Type': 'text/html; encoding=utf8',
            'Connection': 'close',
            'Content-Length': len(self.body)
        }

    def render(self):
        """
        Generate the text for HTTP Response status, headers, and body
        """
        txt = ""
        # status line
        txt += "HTTP/1.1 {} {}\r\n".format(str(self.resp_code),
                                           status_codes[int(self.resp_code)])
        # headers: List comprehension for demo of skill only
        # don't like the hit to readability
        txt += "\r\n".join(["{}: {}".format(k,v) for k, v in self.headers.iteritems()])
        # body
        txt += "\r\n\r\n" + self.doctype + self.body
        return txt
