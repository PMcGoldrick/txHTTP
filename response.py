from common import status_codes, root_dir
import os


class Response(object):
    """
    A default response object
    """
    def __init__(self, resp_code, body=None):
        """
        I build the default reponse, including status line, headers and default html body
        build from status code message.
        """
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
            'Content-Length': len(self.doctype + self.body)
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
        txt += "\r\n".join(["{}: {}".format(k, v) for k, v in self.headers.iteritems()])
        # body
        txt += "\r\n\r\n" + self.doctype + self.body
        return txt


class DirectoryIndexResponse(Response):
    """
    I am a response object that handles listing directories
    on the filesystem.
    """
    def __init__(self, directory):
        """
        I set the appropriate status code and body via my parents `__init__`.
        """
        self.htaccess = None
        # Welcome to path delimiter hell
        os_dir = os.path.join(*directory.split("/"))
        rel_path = os.path.join(root_dir, os_dir)
        if not os.path.isdir(rel_path):
            Response.__init__(self, 404)
        elif not os.path.isfile(os.path.join(rel_path, ".htaccess")):
            Response.__init__(self, 403)
        else:
            with open(os.path.join(rel_path, ".htaccess"), "r") as f:
                self.htaccess = f.read()

            # NOTE: This is definitely shortcutted for time and readability.
            # full spec htaccess implementation would take a while. :)

            # Explicitly forbidden
            if "-Indexes" in self.htaccess:
                Response.__init__(self, 403)
            # Explicitly allowed
            elif "+Indexes" in self.htaccess:
                # `item` is a callable.
                item = '<a href="/{pth}">{name}</a>\n'.format
                # This next line may have gotten a bit... out of control
                # Calls the above for every child _directory_.
                items = ''.join(
                    [item(pth="{}/{}".format(directory, i).strip("/"), name=i) \
                    for i in os.listdir(rel_path) if os.path.isdir(os.path.join(rel_path, i))]
                    )
                body = """<html>
                            <head>
                                <title>Directory listing of {pth}</title>
                            </head>
                            <body>
                                {dirs}
                            </body>
                        </html>""".format(pth=directory, dirs=items)
                Response.__init__(self, 200, body=body)
            else:
                Response.__init__(self, 403)
