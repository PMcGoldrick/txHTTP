txHTTP
======

HTTP server coding challenge. This http server is implemented with twisted line receiver, just so I can avoid socket code and concentrate on the real purpose.
It is only _directory_ aware, and only aware of -Indexes and +Indexes ``htaccess`` declarations.

running
------

``$ python app.py``
``$ trial txHTTP``

resources:
http://www.w3.org/Protocols/rfc2616/rfc2616.html
http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol
http://www.twistedmatrix.com