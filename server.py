#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8085
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CloudflarePagesHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        clean_path = self.path.split('?')[0].rstrip('/')
        if clean_path == '/assets/carta-es.pdf':
            self.send_response(302)
            self.send_header('Location', '/menu')
            self.end_headers()
            return
        if clean_path in ('/menu', '/carta'):
            self.path = '/index.html'
            return super().do_GET()
        return super().do_GET()

    def do_HEAD(self):
        clean_path = self.path.split('?')[0].rstrip('/')
        if clean_path == '/assets/carta-es.pdf':
            self.send_response(302)
            self.send_header('Location', '/menu')
            self.end_headers()
            return
        if clean_path in ('/menu', '/carta'):
            self.path = '/index.html'
            return super().do_HEAD()
        return super().do_HEAD()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CloudflarePagesHandler) as httpd:
        print(f"🌐 Servidor local Bar Luna Llena en http://localhost:{PORT}")
        print("⚡ Simulación Cloudflare Pages (_redirects y rewrites activados)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido.")
