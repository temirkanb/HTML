import os.path
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import time

hostName = "localhost"
serverPort = 8080

ROOT_DIR = os.path.dirname(__file__)


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от
    """
    content_file = os.path.join(ROOT_DIR, 'page', 'webpage.html')

    def get_content_data(self):
        with open(self.content_file, 'r', encoding='utf-8') as file:
            return file.read()

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.get_content_data()
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
