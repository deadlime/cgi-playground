import socketserver
from itertools import batched
from pprint import pformat


class ScgiHandler(socketserver.BaseRequestHandler):
    def handle(self):
        headers_size = b''
        while (data := self.request.recv(1)) != b':':
            headers_size += data
        headers_size = int(headers_size)

        headers_txt = self.request.recv(int(headers_size)).decode('utf-8')

        headers = dict(batched(headers_txt.strip('\0').split('\0'), 2))

        self.request.recv(1)  # extra comma after the headers

        body_size = int(headers['CONTENT_LENGTH'])
        body = self.request.recv(body_size)

        response = (
            'Status: 200 OK\r\n' +
            'Content-Type: text/plain\r\n' +
            '\r\n' +
            'Headers:\n' + pformat(headers) + '\n\n' +
            'Body:\n' + body.decode('utf-8') + '\n'
        ).encode('utf-8')
        self.request.sendall(response)


if __name__ == '__main__':
    with socketserver.TCPServer(('0.0.0.0', 9999), ScgiHandler) as server:
        server.serve_forever()
