"""Serve the two separate pages on one local origin so catalog storage is shared."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import webbrowser

ROOT = Path(__file__).resolve().parent
class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

if __name__ == '__main__':
    server = ThreadingHTTPServer(('127.0.0.1', 8765), Handler)
    print('Loja: http://127.0.0.1:8765/prototipo-loja.html')
    print('Admin: http://127.0.0.1:8765/admin.html')
    print('Painel local sem autenticacao. Ctrl+C encerra o servidor.')
    webbrowser.open('http://127.0.0.1:8765/admin.html')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
