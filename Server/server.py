from http.server import HTTPServer, BaseHTTPRequestHandler
from Services.service_facade import ServiceFacade
import json


# TODO: add checks on each function for the parameters that are required (ex: when creating a new user, we need the
#  username, first name, etc., so make sure all of those are passed in)
# TODO: add docs and tests
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
        self.send_response(code)
        # Do we need this?
        # self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        if self.path == '/getAvailablePairs':
            available_pairs, error_message = self.service_facade.get_available_currency_pairs()

            if error_message is not None:
                self._send_response(404)
                self.wfile.write(error_message.encode())
                return

            pairs = []

            for pair in available_pairs:
                pairs.append(pair[0])

            pairs_json = json.dumps(pairs)

            self._send_response(200)
            self.wfile.write(pairs_json.encode())

        elif self.path == '/getPairsFollowed':
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len).decode('utf-8')
            request_body = self._format_request_body(post_body)

            user_id = request_body['user_id']

            followed_pairs_for_user, error_message = self.service_facade.get_pairs_followed_for_user(user_id)

            if error_message is not None:
                self._send_response(404)
                self.wfile.write(error_message.encode())
                return

            followed_pairs = []

            for pair in followed_pairs_for_user:
                followed_pairs.append(pair[0])

            followed_pairs_json = json.dumps(followed_pairs)

            self._send_response(200)
            self.wfile.write(followed_pairs_json.encode())

        elif self.path == '/getFollowedPairsLeft':
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len).decode('utf-8')
            request_body = self._format_request_body(post_body)

            user_id = request_body['user_id']

            pairs_left, error_message = self.service_facade.get_followed_pairs_left_for_user(user_id)

            if error_message is not None:
                self._send_response(404)
                self.wfile.write(error_message.encode())
                return

            pairs_left_json = json.dumps(pairs_left[0])

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

        elif self.path == '/getMonthlyBill':
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len).decode('utf-8')
            request_body = self._format_request_body(post_body)

            user_id = request_body['user_id']

            monthly_bill, error_message = self.service_facade.get_monthly_bill(user_id)

            if error_message is not None:
                self._send_response(404)
                self.wfile.write(error_message.encode())
                return

            monthly_bill_json = json.dumps(monthly_bill[0])

            self._send_response(200)
            self.wfile.write(monthly_bill_json.encode())

    def do_POST(self):
        if self.path == '/updatePairsFollowed':
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len).decode('utf-8')
            request_body = self._format_request_body(post_body)

            user_id = request_body['user_id']
            currency_pair_name = request_body['currency_pair_name']

            message = self.service_facade.update_pairs_followed_for_user(user_id, currency_pair_name)

            if message != 'Successfully updated pairs followed':
                self._send_response(404)
                self.wfile.write(message.encode())
                return

            self._send_response(200)

        elif self.path == '/updateSubscription':
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len).decode('utf-8')
            request_body = self._format_request_body(post_body)

            user_id = request_body['user_id']
            subscription_type = request_body['subscription_type']

            message = self.service_facade.update_subscription(user_id, subscription_type)

            if message != 'Updated subscription':
                self._send_response(404)
                self.wfile.write(message.encode())
                return

            self._send_response(200)

        elif self.path == '/createUser':
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len).decode('utf-8')
            request_body = self._format_request_body(post_body)

            username = request_body['username']
            first_name = request_body['first_name']
            last_name = request_body['last_name']
            password = request_body['password']
            subscription_type = request_body['subscription_type']

            user_id, error_message = self.service_facade.create_user(username, first_name, last_name, password,
                                                                     subscription_type)

            if error_message is not None:
                self._send_response(404)
                self.wfile.write(error_message.encode())
                return

            user_id_json = json.dumps(user_id)

            self._send_response(200)
            self.wfile.write(user_id_json.encode())

        elif self.path == '/login':
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len).decode('utf-8')
            request_body = self._format_request_body(post_body)

            username = request_body['username']
            password = request_body['password']

            user_id, error_message = self.service_facade.login(username, password)

            if error_message is not None:
                self._send_response(404)
                self.wfile.write(error_message.encode())
                return

            user_id_json = json.dumps(user_id[0])

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
