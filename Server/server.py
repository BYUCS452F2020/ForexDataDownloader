from http.server import HTTPServer, BaseHTTPRequestHandler
from Services.service_facade import ServiceFacade
import json


# TODO: implement and add docs/comments
class Handler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        self.service_facade = ServiceFacade()
        self.request_id = BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def _format_request_body(self, body):
        key_val_pairs = body.split('&')
        request_body = {}

        for pair in key_val_pairs:
            key, val = pair.split('=')
            request_body[key] = val

        return request_body

    def _send_response(self, code):
        # TODO: code is 200 (success) or 404/other failure code
        self.send_response(code)
        # TODO: do we need this?
        # self.send_header('Content-type', 'text/html')
        self.end_headers()

    # TODO: check for errors and send 404 responses accordingly
    # TODO: add docs/comments
    # TODO: double check that everything aligns properly with the service facade (items that are returned, input parameters, etc.)
    # TODO: test everything
    def do_GET(self):
        if self.path == '/getAvailablePairs':
            pairs = self.service_facade.get_available_currency_pairs()
            pairs_json = json.dumps(pairs)

            self._send_response(200)

            self.wfile.write(pairs_json.encode())

        elif self.path == '/getPairsFollowed':
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len).decode('utf-8')
            request_body = self._format_request_body(post_body)

            user_id = request_body['user_id']

            followed_pairs = self.service_facade.get_pairs_followed_for_user(user_id)
            followed_pairs_json = json.dumps(followed_pairs)

            self._send_response(200)

            self.wfile.write(followed_pairs_json.encode())

        elif self.path == '/getFollowedPairsLeft':
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len).decode('utf-8')
            request_body = self._format_request_body(post_body)

            user_id = request_body['user_id']

            pairs_left = self.service_facade.get_followed_pairs_left_for_user(user_id)
            pairs_left_json = json.dumps(pairs_left)

            self._send_response(200)

            self.wfile.write(pairs_left_json.encode())

        elif self.path == '/getHistoricalData':
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len).decode('utf-8')
            request_body = self._format_request_body(post_body)

            currency_pair = request_body['currency_pair']
            time_frame_granularity = request_body['time_frame_granularity']
            from_time = request_body['from_time']
            from_time = from_time.replace('+', ' ')
            from_time = from_time.replace('%3A', ':')
            to_time = request_body['to_time']
            to_time = to_time.replace('+', ' ')
            to_time = to_time.replace('%3A', ':')

            candles, error_message = self.service_facade.get_historical_data(currency_pair, time_frame_granularity,
                                                                             from_time, to_time)
            if error_message is not None:
                self._send_response(404)
                self.wfile.write(error_message.encode())

            else:
                candles_json = candles.to_json(orient='records')

                self._send_response(200)

                self.wfile.write(candles_json.encode())

    # TODO: check for errors and send 404 responses accordingly
    # TODO: add docs/comments
    # TODO: double check that everything aligns properly with the service facade (items that are returned, input parameters, etc.)
    # TODO: test everything
    def do_POST(self):
        if self.path == '/updatePairsFollowed':
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len).decode('utf-8')
            request_body = self._format_request_body(post_body)

            user_id = request_body['user_id']
            currency_pair_name = request_body['currency_pair_name']

            self.service_facade.update_pairs_followed_for_user(user_id, currency_pair_name)

            self._send_response(200)

        elif self.path == '/updateSubscription':
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len).decode('utf-8')
            request_body = self._format_request_body(post_body)

            user_id = request_body['user_id']
            subscription_type = request_body['subscription_type']

            self.service_facade.update_subscription(user_id, subscription_type)

            self._send_response(200)

        elif self.path == '/createUser':
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len).decode('utf-8')
            request_body = self._format_request_body(post_body)

            username = request_body['username']
            first_name = request_body['first_name']
            last_name = request_body['last_name']
            subscription_type = request_body['subscription_type']

            user_id = self.service_facade.create_user(username, first_name, last_name, subscription_type)
            user_id_json = json.dumps(user_id)

            self._send_response(200)

            self.wfile.write(user_id_json.encode())

        elif self.path == '/login':
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len).decode('utf-8')
            request_body = self._format_request_body(post_body)

            username = request_body['username']
            password = request_body['password']

            user_id = self.service_facade.login(username, password)
            user_id_json = json.dumps(user_id)

            self._send_response(200)

            self.wfile.write(user_id_json.encode())


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
