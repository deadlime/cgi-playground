import socketserver
from pprint import pformat

FCGI_END_REQUEST = 3
FCGI_PARAMS = 4
FCGI_STDIN = 5
FCGI_STDOUT = 6


class FcgiHandler(socketserver.BaseRequestHandler):
    def handle(self):
        params_data = b''
        body = b''
        last_header = b''

        params_finished = False
        stdin_finished = False
        while not (params_finished and stdin_finished):
            last_header = header = self.__parse_fcgi_header(self.request.recv(8))
            content = self.request.recv(header['content_length'])
            self.request.recv(header['padding_length'])  # ignore padding

            if header['type'] == FCGI_PARAMS:
                params_data += content
                if not content:
                    params_finished = True
            if header['type'] == FCGI_STDIN:
                body += content
                if not content:
                    stdin_finished = True

        params = self.__parse_params(params_data)

        response = (
            'Content-Type: text/plain\r\n' +
            '\r\n' +
            'Params:\n' + pformat(params) + '\n\n' +
            'Body:\n' + body.decode('utf-8') + '\n'
        ).encode('utf-8')

        request_id = last_header['request_id'].to_bytes(2, 'big')

        self.request.sendall(b'\x01' + FCGI_STDOUT.to_bytes(1, 'big') + request_id + len(response).to_bytes(2, 'big') + b'\0\0' + response)
        self.request.sendall(b'\x01' + FCGI_STDOUT.to_bytes(1, 'big') + request_id + b'\0\0\0\0')
        self.request.sendall(b'\x01' + FCGI_END_REQUEST.to_bytes(1, 'big') + request_id + b'\0\x08\0\0' + b'\0\0\0\0\0\0\0\0')

    def __parse_fcgi_header(self, data):
        return {
            'version': data[0],
            'type': data[1],
            'request_id': int.from_bytes(data[2:4], 'big'),
            'content_length': int.from_bytes(data[4:6], 'big'),
            'padding_length': data[6],
        }

    def __parse_params(self, data):
        idx = 0
        params = {}
        while idx < len(data):
            key_length = data[idx]
            idx += 1
            value_length = data[idx]
            idx += 1

            key = data[idx:idx + key_length]
            idx += key_length
            value = data[idx:idx + value_length]
            idx += value_length

            params[key] = value

        return params


if __name__ == '__main__':
    with socketserver.TCPServer(('0.0.0.0', 9999), FcgiHandler) as server:
        server.serve_forever()
