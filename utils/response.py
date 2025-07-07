from flask import Response
import json

default_headers = { 'Content-Type': 'application/json' }

class DefaultResponse(Response):
    def __init__(self, response, status=200, headers=default_headers, mimetype=None, content_type=None, direct_passthrough=None):
        super().__init__(json.dumps(response), status, headers, mimetype, content_type, direct_passthrough)