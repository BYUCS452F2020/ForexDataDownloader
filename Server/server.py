from http.server import HTTPServer, BaseHTTPRequestHandler
from Services.service_facade import ServiceFacade


# TODO: implement and add docs/comments
class Handler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        self.request_id = BaseHTTPRequestHandler.__init__(self, request, client_address, server)
        self.service_facade = ServiceFacade()

    def _format_request_body(self, body):
        key_val_pairs = body.split('&')
        request_body = {}

        for pair in key_val_pairs:
            key, val = pair.split('=')
            request_body[key] = val

        return request_body

    def _send_response(self, code):
        self.send_response(200)
        # TODO: do we need this?
        # self.send_header('Content-type', 'text/html')
        self.end_headers()

    # TODO: implement this
    def do_GET(self):
        # TODO: change this path to a real service we have and implement it as such
        if self.path == '/test':
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len).decode('utf-8')
            request_body = self._format_request_body(post_body)
            self._send_response(200)
            self.wfile.write('Hello'.encode())

    # TODO: implement this
    def do_POST(self):
        pass



def main():
    # Server port
    PORT = 8080

    # Server address
    address = 'localhost'
    server_address = (address, PORT)

    # Create the server
    server = HTTPServer(server_address, Handler)
    print('Server running on port: ' + str(PORT))

    # Run the server until cancelled
    server.serve_forever()


if __name__ == '__main__':
    main()
